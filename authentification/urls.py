from django.urls import path
from .views import RegistrationView

app_name = "authentification" # espace de noms

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    # path('connexion/', ConnexionView.as_view(), name="connexion"),
]
