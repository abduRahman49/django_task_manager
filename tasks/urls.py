from django.urls import path
from .views import ProjectView, home_view, project_list_view, delete_project_view, project_detail_view

app_name = "tasks" # espace de noms

urlpatterns = [
    path('projects/new', ProjectView.as_view(), name="create"),
    path('projects/list', project_list_view, name="list"),
    path('projects/<project_id>/delete', delete_project_view, name="delete"),
    path('projects/<project_id>/detail', project_detail_view, name="detail"),
    path('home/', home_view, name="home")
]
