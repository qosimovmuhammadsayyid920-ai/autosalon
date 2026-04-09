from django.shortcuts import render
from .models import Brand, Car
from django.http import HttpRequest


def home(request: HttpRequest):
    brands = Brand.objects.all()
    car = Car.objects.all()

    context = {
        'brands': brands,
        'car': car,
        'title': 'AutoSalon'
    }

    return render(request, 'autoapp/home.html', context)

def car_by_brand(request: HttpRequest, brand_id: int):
    brands = Brand.objects.get(id=brand_id)
    brand = Brand.objects.get(pk=brand_id)
    cars = Car.objects.filter(brand=brand)

    context = {
        'brands': brands,
        'cars': cars,
        'title': brand.name
    }
    return render(request, 'autoapp/car_by_brand.html', context)

def one_car(request: HttpRequest, car_id: int):
    cars = Car.objects.get(id=car_id)

    context = {
        'cars': cars
    }

    return render(request, 'autoapp/one_car.html', context)


def add_car(request: HttpRequest):
    print(request.POST)
    return render(request, 'autoapp/add_car.html')
