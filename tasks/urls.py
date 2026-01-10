from django.urls import path
from .views import ProjectView

urlpatterns = [
    path('projects/new', ProjectView.as_view()),
]
