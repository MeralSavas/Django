from django.shortcuts import render
from django.http import HttpResponse




def home(request):
    return render(request, 'students/home.html')

    # return HttpResponse('<p> Hello </p>')
