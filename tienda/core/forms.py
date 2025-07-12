from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    edad = forms.IntegerField(min_value=0)
    telefono = forms.CharField(max_length=15)

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'edad', 'telefono', 'password1', 'password2']





class AgregarAlCarritoForm(forms.Form):
    producto_id = forms.IntegerField(widget=forms.HiddenInput())
    cantidad = forms.IntegerField(min_value=1, initial=1)
