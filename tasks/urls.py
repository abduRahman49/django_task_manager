from django.urls import path
from .views import ProjectView, home_view

app_name = "tasks" # espace de noms

urlpatterns = [
    path('projects/new', ProjectView.as_view(), name="create"),
    path('home/', home_view, name="home")
]
