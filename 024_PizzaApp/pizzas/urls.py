from django.urls import path
from .views import home, pizzas, order_view

urlpatterns = [
    path('', home, name='home'),
    path('pizzas/', pizzas, name='pizzas'),
    path('pizzas/<int:id>', order_view, name='order'),
]