from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cities/', views.city_list, name='cities'),
    path('cities/<int:city_id>/', views.detail, name='detail'),
    path('form/', views.new_form, name='form'),
]