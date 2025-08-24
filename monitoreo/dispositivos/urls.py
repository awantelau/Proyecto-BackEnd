from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('panel/', views.panel_dispositivos, name='panel'),
]