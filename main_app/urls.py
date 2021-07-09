from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('cities/', views.city_list, name='cities'),
    path('cities/<int:city_id>/', views.detail, name='detail'),
    path('form/', views.new_form, name='form'),
    path('cities/<int:pk>/update/', views.CityUpdate.as_view(), name='cities_update'),
    path('cities/<int:pk>/delete/', views.CityDelete.as_view(), name='cities_delete'),
    path('cities/<int:city_id>/add_spot/', views.add_spot, name='add_spot'),
  
    path('cities/<int:city_id>/assoc_airline/<int:airline_id>/', views.assoc_airline, name='assoc_airline'),
    path('cities/<int:city_id>/unassoc_airline/<int:airline_id>/', views.unassoc_airline, name='unassoc_airline'),

    path('airlines/', views.AirlineList.as_view(), name='airline_index'),

    path('airlines/<int:pk>/', views.AirlineDetail.as_view(), name='airline_detail'),
    
    path('airlines/create/', views.AirlineCreate.as_view(), name='airline_create'),
    
    path('accounts/signup/', views.signup, name='signup'),

    path('cities/<int:city_id>/add_photo/', views.add_photo, name='add_photo'),
]