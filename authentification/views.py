from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm

# Create your views here.
class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, "authentification/registration.html", {"form": form})