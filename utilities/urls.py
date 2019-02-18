from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('bye/', views.bye),
    path('graduation/', views.graduation),
    path('imagepick/', views.imagepick),
    path('today/', views.today),
    path('ascii_new/', views.ascii_new),
    path('ascii_make/', views.ascii_make),
    path('original/', views.original),
    path('translated/', views.translated),
]