from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formularioContacto/', views.contactar, name='contactar'),
    path('admin/', views.index, name='admin'),
]