from django.shortcuts import render


def home(request):
    return render(request, 'pizzas/home.html')

def pizzas(request):
    return render(request, 'pizzas/pizzas.html')