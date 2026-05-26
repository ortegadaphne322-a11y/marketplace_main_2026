from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Product

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        from django.contrib.auth import get_user_model
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})