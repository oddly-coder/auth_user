from django.shortcuts import render
from django.contrib import messages
from .forms import RegistrationForm

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'An account has being created for {username}')
    else:
        form =RegistrationForm()
    return render(request, 'register.html', {'form': form})
