from django.urls import path
from .views import RegistrationView

app_name = "authentification" # espace de noms

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    # path('projects/list', ProjectListView.as_view(), name="list"),
]
