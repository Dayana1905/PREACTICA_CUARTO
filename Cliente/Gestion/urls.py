from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.crear_cliente, name='crear_cliente'),  
# Crear cliente
    path('clientes/listar/', views.listar_clientes, name='listar_clientes'),  
# Listar clientes
    path('clientes/<int:pk>/', views.obtener_cliente, name='obtener_cliente'), 
 # Obtener cliente por ID
    path('clientes/<int:pk>/actualizar/', views.actualizar_cliente, name='actualizar_cliente'),
  # Actualizar cliente
    path('clientes/<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),  
# Eliminar cliente
]
