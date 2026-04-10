from django.urls import path
from .views import home, one_car, car_by_brand, add_brand, add_car

urlpatterns = [
    path('', home, name='home'),
    path('brand/<int:brand_id>/', car_by_brand, name='car_by_brand'),
    path('car/<int:car_id>/', one_car, name='one_car'),
    path('brand/add/', add_brand, name='add_brand'),
    path('car/add/', add_car, name='add_car')
    
]
