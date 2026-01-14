from django.urls import path
from .views import ProjectView

app_name = "tasks" # espace de noms

urlpatterns = [
    path('projects/new', ProjectView.as_view(), name="create"),
    # path('projects/list', ProjectListView.as_view(), name="list"),
]
