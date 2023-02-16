from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Student
from .forms import StudentForm




def home(request):

    context = {
        'title': 'clarusway',
        'desc': 'This is a description',
        'number': 1111,
        'list1': ['a', 1, 'b', ['c', 2]],
        'dict1': {
            'key1': 'value1',
            'key2': 'value2'
        },
        'dict_list': [
            {'name': 'zed', 'age': 25},
            {'name': 'amy', 'age': 21},
            {'name': 'joe', 'age': 50},
        ]

    }


    return render(request, 'students/home.html', context)

    # return HttpResponse('<p> Hello </p>')


    '''
{{ variables }}
{% command %}
| ---> filter
'''

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }

    return render(request, 'students/student_list.html', context)

def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        # print('POST :', request.POST) img yi yakalamadi bos donderdi
        # print('fıles :', request.FILES) img yi yakaladi enctype="multipart/form-data" ekle
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    context = {
        'form': form
    }


    return render(request, 'students/student_add.html', context)