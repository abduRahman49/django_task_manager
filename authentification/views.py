from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import RegistrationForm, ConnexionForm
from .services import AuthenticationService
from core.exceptions import UserAlreadyExists


# Vue permettant de créer un nouvel utilisateur
class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, "authentification/registration.html", {"form": form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = AuthenticationService.register_user(
                    data.get("username"),
                    data.get("email"),
                    data.get("password"),
                    data.get("name"),
                    data.get("surname")
                )
            except UserAlreadyExists as e:
                form.add_error(None, e.message)
                return render(request, "authentification/registration.html", {"form": form})
            
            messages.add_message(request, messages.INFO, "Connexion réussie")
            return redirect("authentification:connexion")

        return render(request, "authentification/registration.html", {"form": form})

# Vue permettant de se connecter
class ConnexionView(View):

    def get(self, request):
        form = ConnexionForm()
        return render(request, "authentification/connexion_form.html", {"form": form})

    
    def post(self, request):
        form = ConnexionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get("username")
            password = data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect("tasks:home")
            else:
                # Return an 'invalid login' error message.
                messages.add_message(request, messages.ERROR, "Cet utilisateur n'existe pas, veuillez réessayer")
                return render(request, "authentification/connexion_form.html", {"form": form})
        
        return render(request, "authentification/connexion_form.html", {"form": form})
