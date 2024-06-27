from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contactar, name='contactar'),
    path('admin/', views.index, name='admin'),
]