from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto, Categoria, Etiqueta

def index(request):
    return render(request, 'tienda/index.html')

class ProductoListView(ListView):
    model = Producto
    template_name = 'tienda/productos/lista.html'
    context_object_name = 'productos'

    # Ejemplo de consulta con ORM
    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtra por nombre si se pasa el parámetro 'q' en la URL
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        # Excluye productos con precio 0
        queryset = queryset.exclude(precio=0)
        return queryset

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'tienda/productos/detalle.html'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'tienda/productos/crear.html' # Cambiado de formulario.html
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']
    success_url = reverse_lazy('tienda:lista_productos')

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'tienda/productos/editar.html' # Cambiado de formulario.html
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']
    success_url = reverse_lazy('tienda:lista_productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'tienda/productos/eliminar.html'
    success_url = reverse_lazy('tienda:lista_productos')

# Asigna las vistas basadas en clases a los nombres de funciones que usaste en urls.py
lista_productos = ProductoListView.as_view()
detalle_producto = ProductoDetailView.as_view()
crear_producto = ProductoCreateView.as_view()
editar_producto = ProductoUpdateView.as_view()
eliminar_producto = ProductoDeleteView.as_view()

# Vistas para Categoría
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'tienda/categorias/lista.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'tienda/categorias/formulario.html'
    fields = ['nombre']
    success_url = reverse_lazy('tienda:lista_categorias')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'tienda/categorias/formulario.html'
    fields = ['nombre']
    success_url = reverse_lazy('tienda:lista_categorias')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    # Se debe usar una plantilla de confirmación. Reutilizamos la de productos.
    template_name = 'tienda/productos/eliminar.html' 
    success_url = reverse_lazy('tienda:lista_categorias')

lista_categorias = CategoriaListView.as_view()
crear_categoria = CategoriaCreateView.as_view()
editar_categoria = CategoriaUpdateView.as_view()
eliminar_categoria = CategoriaDeleteView.as_view()


# Vistas para Etiqueta
class EtiquetaListView(ListView):
    model = Etiqueta
    template_name = 'tienda/etiquetas/lista.html'
    context_object_name = 'etiquetas'

class EtiquetaCreateView(CreateView):
    model = Etiqueta
    template_name = 'tienda/etiquetas/formulario.html'
    fields = ['nombre']
    success_url = reverse_lazy('tienda:lista_etiquetas')

class EtiquetaUpdateView(UpdateView):
    model = Etiqueta
    template_name = 'tienda/etiquetas/formulario.html'
    fields = ['nombre']
    success_url = reverse_lazy('tienda:lista_etiquetas')

class EtiquetaDeleteView(DeleteView):
    model = Etiqueta
    # Se debe usar una plantilla de confirmación. Reutilizamos la de productos.
    template_name = 'tienda/productos/eliminar.html'
    success_url = reverse_lazy('tienda:lista_etiquetas')

lista_etiquetas = EtiquetaListView.as_view()
crear_etiqueta = EtiquetaCreateView.as_view()
editar_etiqueta = EtiquetaUpdateView.as_view()
eliminar_etiqueta = EtiquetaDeleteView.as_view()
