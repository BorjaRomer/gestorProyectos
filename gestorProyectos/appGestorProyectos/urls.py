from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.show_proyecto_form, name='proyecto_form'),
    path('proyecto/', views.post_proyecto_form, name='post_proyecto_form'),

]
