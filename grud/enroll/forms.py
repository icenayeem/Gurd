from django import forms
from django.core import validators
from django.forms import fields, models, widgets
from .models import studentin
class studentregistation(models.ModelForm):
    class Meta:
        model = studentin
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'})
        }