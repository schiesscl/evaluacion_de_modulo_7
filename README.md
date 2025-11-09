# Evaluación de Módulo 7 - Sistema de Gestión de Tienda

## Hans Schiess

### Propósito y Alcance

Este documento proporciona una visión general de alto nivel del proyecto Django `evaluacion_modulo_7`, una aplicación web para la gestión de productos. Introduce la arquitectura del proyecto, las entidades principales, la pila tecnológica y los componentes clave. Esta página sirve como punto de entrada para comprender el sistema antes de profundizar en subsistemas específicos.

### Resumen del Proyecto

`evaluacion_modulo_7` es una aplicación web basada en Django que implementa un sistema de gestión de catálogo de productos (denominado `tienda`). La aplicación permite a los usuarios gestionar productos, categorías y etiquetas a través de una interfaz web con operaciones completas de Crear, Leer, Actualizar y Eliminar (CRUD).

El sistema se organiza en torno a tres entidades principales definidas en [`tienda/models.py`](./evaluacion_modulo_7/tienda/models.py):

* **Producto**: La entidad principal que representa los artículos en el catálogo.
* **Categoría**: Un sistema de clasificación para los productos.
* **Etiqueta**: Un sistema de etiquetado flexible para la organización de productos.

---

## Pila Tecnológica

| Componente | Tecnología | Versión/Detalles |
| :--- | :--- | :--- |
| Framework Web | Django | 5.2.8 |
| Base de Datos | PostgreSQL | Base de datos: `evaluacion_modulo_7_db` |
| Motor de Plantillas | Django Templates | Con herencia de plantillas |
| Framework Frontend | Bootstrap | 5.3.3 (vía CDN) |
| Arquitectura de Vistas | Vistas Basadas en Clases de Django | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| ORM | Django ORM | Con API de `QuerySet` |
| Interfaz de Admin | Django Admin | Sitio de administración incorporado |

El proyecto utiliza ampliamente las características incorporadas de Django, incluyendo la interfaz de administración, el middleware de autenticación, la protección CSRF y la herencia de plantillas.

---

## Guía de Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### Requisitos Previos

* Python (versión 3.8 o superior)
* pip (generalmente viene con Python)
* Git
* Un servidor de PostgreSQL en ejecución.

### Instalación y Configuración

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/schiesscl/evaluacion_de_modulo_7.git
    cd evaluacion_de_modulo_7
    ```

2. **Crear y activar un entorno virtual:**

    ```bash
    # Crear el entorno virtual
    python -m venv venv

    # Activar en Windows
    .\venv\Scripts\activate

    # Activar en macOS/Linux
    source venv/bin/activate
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar la base de datos:**
    Abre el archivo [`evaluacion_modulo_7/settings.py`](./evaluacion_modulo_7/evaluacion_modulo_7/settings.py) y modifica la sección `DATABASES` con tus credenciales de PostgreSQL.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nombre_de_tu_db',        # Reemplazar
            'USER': 'tu_usuario_postgres',   # Reemplazar
            'PASSWORD': 'tu_contraseña',     # Reemplazar
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Aplicar las migraciones:**

    ```bash
    python manage.py migrate
    ```

6. **Crear un superusuario:**
    Necesitarás un superusuario para acceder al panel de administración.

    ```bash
    python manage.py createsuperuser
    ```

### Ejecución

Una vez completada la instalación, puedes iniciar el servidor de desarrollo.

```bash
python manage.py runserver
```

La aplicación estará disponible en **`http://127.0.0.1:8000/`**.
Puedes acceder al panel de administración en **`http://127.0.0.1:8000/admin/`**.

### Poblar la base de datos (Opcional)

Para probar la aplicación con datos de ejemplo, abre el shell de Django:

```bash
python manage.py shell
```

Y luego, pega el siguiente script:

```python
from tienda.models import Categoria, Etiqueta, Producto, DetallesProducto

Producto.objects.all().delete()
Categoria.objects.all().delete()
Etiqueta.objects.all().delete()
DetallesProducto.objects.all().delete()

cat_tecnologia = Categoria.objects.create(nombre='Tecnología')
cat_libros = Categoria.objects.create(nombre='Libros')
cat_deportes = Categoria.objects.create(nombre='Deportes')

tag_oferta = Etiqueta.objects.create(nombre='Oferta')
tag_nuevo = Etiqueta.objects.create(nombre='Nuevo')
tag_mas_vendido = Etiqueta.objects.create(nombre='Más Vendido')

p1 = Producto.objects.create(nombre='Smartphone X-100', descripcion='El último modelo con cámara de 108MP.', precio=699.99, categoria=cat_tecnologia)
p1.etiquetas.add(tag_nuevo, tag_mas_vendido)
DetallesProducto.objects.create(producto=p1, dimensiones='160x75x8 mm', peso=0.194)

p2 = Producto.objects.create(nombre='El Jardín de las Sombras', descripcion='Novela de misterio y fantasía.', precio=19.95, categoria=cat_libros)
p2.etiquetas.add(tag_mas_vendido)
DetallesProducto.objects.create(producto=p2, peso=0.450)

print("Datos de ejemplo creados exitosamente.")
```

---

## Arquitectura y Diseño del Sistema

### Estructura del Proyecto

*Diagrama de la relación entre los archivos de configuración del proyecto Django, los componentes de la aplicación `tienda` y la base de datos PostgreSQL.*

### Entidades y Relaciones del Núcleo

El sistema implementa tres entidades principales con relaciones específicas definidas en el ORM de Django.

| Relación | Tipo | Comportamiento de Eliminación | Opcional |
| :--- | :--- | :--- | :--- |
| `Producto.categoria` → `Categoria` | `ForeignKey` | `PROTECT` | No |
| `Producto.etiquetas` → `Etiqueta` | `ManyToMany` | N/A | Sí (`blank=True`) |
| `DetallesProducto.producto` → `Producto` | `OneToOne` | `CASCADE` | No |

El comportamiento `PROTECT` en `Producto.categoria` evita la eliminación de una categoría si existen productos asociados, asegurando la integridad referencial. `CASCADE` en `DetallesProducto.producto` asegura que los detalles se eliminen cuando se elimina el producto padre.

### Arquitectura de Operaciones CRUD

Cada entidad tiene un conjunto completo de vistas basadas en clases que implementan las operaciones CRUD.

*Mapa de las vistas basadas en clases de Django y sus patrones de URL correspondientes en la aplicación `tienda`.*

### Puntos de Entrada y Enrutamiento

La página de inicio, renderizada por la vista `index`, sirve como punto de entrada a la aplicación, proporcionando navegación directa a las listas de productos, categorías y etiquetas.

### Estructura de Herencia de Plantillas

Todas las plantillas heredan de [`base.html`](./evaluacion_modulo_7/tienda/templates/tienda/base.html), que proporciona la estructura común (Bootstrap, barra de navegación, footer).

*Todas las plantillas extienden de `base.html`. Se reutiliza `productos/eliminar.html` para las confirmaciones de eliminación de categorías y etiquetas.*

---

## Características Clave y Seguridad

### Funcionalidades de Gestión

* **Búsqueda**: La lista de productos implementa una búsqueda insensible a mayúsculas por nombre.
* **Filtros**: Se excluyen automáticamente los productos con precio cero.
* **Interfaz de Admin**: Todos los modelos están registrados en el [sitio de administración de Django](./evaluacion_modulo_7/tienda/admin.py), proporcionando una interfaz de gestión alternativa.

### Configuración de Seguridad

La aplicación implementa la pila de middleware de seguridad de Django, incluyendo protección contra CSRF, gestión de sesiones y prevención de clickjacking.

> **Nota**: La configuración actual muestra `DEBUG = True` y expone la `SECRET_KEY` en [`settings.py`](./evaluacion_modulo_7/evaluacion_modulo_7/settings.py). Esto indica una configuración de desarrollo que requiere ser robustecida antes de un despliegue en producción.
