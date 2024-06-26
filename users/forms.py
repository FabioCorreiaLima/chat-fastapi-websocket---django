from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Evento

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'data', 'descricao']
