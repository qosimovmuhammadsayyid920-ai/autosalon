from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('brand/<int:brand_id>/', views.car_by_brand, name='car_by_brand'),
    path('car/<int:car_id>/', views.one_car, name='one_car'),
    path('brand/add/', views.add_brand, name='add_brand'),
    path('car/add/', views.add_car, name='add_car'),
    path('brand/<int:brand_id>/update/', views.update_brand, name='update_brand'),
    path('car/<int:car_id>/update/', views.update_car, name='update_car'),
    path('brand/<int:brand_id>/delete/', views.delete_brand, name='delete_brand'),
    path('car/<int:car_id>/delete/', views.delete_car, name='delete_car')
    
]
