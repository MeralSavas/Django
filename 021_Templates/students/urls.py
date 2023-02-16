
from django.urls import path
from .views import (
    home,
    student_list,
    student_add,
)
urlpatterns = [
    path('', home, name='home'),
    path('list/', student_list, name='student_list'),
    path('add/', student_add, name='student_add'),
    
]   