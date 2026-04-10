from django.shortcuts import render, redirect
from .models import Brand, Car
from django.http import HttpRequest
from .forms import BrandForm, CarForm


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


def add_brand(request: HttpRequest):
    if request.method == 'POST':
        form = BrandForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            brand = form.save()
            return redirect('car_by_brand', brand_id=brand.id)
    else:
        form = BrandForm()
    context = {
        'form': form
    }
    return render(request, 'autoapp/add_brand.html', context)

def add_car(request: HttpRequest):
    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            car = form.save()
            return redirect('one_car', car_id=car.id)
    else:
        form = CarForm()
    context = {
        'form': form
    }

    return render(request, 'autoapp/add_car.html', context)