from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
            return redirect('home')

    context = {
        "form": form
    }
    return render(request,'users/register.html', context)
