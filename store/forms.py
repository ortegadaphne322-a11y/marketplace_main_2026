from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Product

# Formulario para el registro de usuarios (Sprint 2 / 3)
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'is_seller',)

# Formulario para la gestión de productos (Sprint 3)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }