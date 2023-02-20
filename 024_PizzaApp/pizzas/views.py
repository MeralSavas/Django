from django.shortcuts import render
from .models import Pizza


def home(request):
    return render(request, 'pizzas/home.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    
    context = {
        'pizzas': pizzas
    }

    return render(request, 'pizzas/pizzas.html', context)

def order_view(request, id):
    return render(request, 'pizzas/order.html')