from django.core.exceptions import PermissionDenied
from .models import Project


class ProjectService:

    @staticmethod
    def create_project(title, owner):
        return Project.objects.create(title=title, owner=owner)

    @staticmethod
    def get_user_projects(user):
        return Project.objects.filter(owner=user)

    @staticmethod
    def delete_project(project_id, user):
        project = Project.objects.get(id=project_id)
        if project.owner != user:
            raise PermissionDenied("Vous n'êtes pas autorisé à supprimer ce projet")

        project.delete()
