from django import forms
from .models import Contact, Service
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


#Formulario de contacto
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ["name", "email", "query_type", "message", "advice"]


#Formulario para agregar un servicio        
class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = '__all__'

#Formulario de registro de usuario
class RegisterForm(UserCreationForm):
    
    def clean_name(self):
        username =self.cleaned_data["name"]
        exist = User.objects.filter(username=username).exists()
        if exist:
            raise ValidationError("A user with that name already exists")
        return username
    
    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email", "password1", "password2"]

