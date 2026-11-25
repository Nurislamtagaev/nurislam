from django.http import HttpResponse
from django.shortcuts import render
from .models import Lalafo, Category


def hello(request):
    category = Category.objects.all()

    return render(request, 'home.html', {
        'category': category,
    })


def my_transport(request):
    products = Lalafo.objects.filter(category__title='Транспорт')
    return render(request, 'products.html', {
        'products': products,
    })

def nedvijimost(request):
    products = Lalafo.objects.filter(category__title='Недвижимость')
    return render(request, 'products.html', {
        'products': products,
    })
