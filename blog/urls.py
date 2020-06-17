from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'index'),    
    path('generales/',views.generales, name = 'generales'),
    path('programacion/',views.programacion, name = 'programacion'),
    path('tecnologia/',views.tecnologia, name = 'tecnologia'),
    path('tutoriales/',views.tutoriales, name = 'tutoriales'),
    path('videojuegos/',views.videojuegos, name = 'videojuegos'),
    path('<slug:slug>/',views.detallePost, name = 'post'),
]


