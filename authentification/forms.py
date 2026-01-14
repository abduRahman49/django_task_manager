from django import forms
from django.forms import ValidationError


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=150, label="Prénom")
    surname = forms.CharField(max_length=150, label="Nom")
    username = forms.CharField(max_length=150, label="Nom d'utilisateur")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise ValidationError("Le mot de passe doit faire au minimum 8 caractères")

        return password


class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=150, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")