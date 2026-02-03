from django.urls import path
from .views import ProjectView, home_view, project_list_view

app_name = "tasks" # espace de noms

urlpatterns = [
    path('projects/new', ProjectView.as_view(), name="create"),
    path('projects/list', project_list_view, name="list"),
    path('home/', home_view, name="home")
]
