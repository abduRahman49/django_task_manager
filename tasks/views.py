from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import ProjectForm
from .services import ProjectService


# CBV (Class Based View)
class ProjectView(View):

    def post(self, request):
        # request.POST => contient les informations de l'utilisateur
        form = ProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            owner = request.user
            project = ProjectService.create_project(data.get("title"), owner)
            messages.add_message(request, messages.SUCCESS, f"Le projet {project.title} a bien été créé")
            return redirect("tasks:create")


    def get(self, request):
        form = ProjectForm()
        return render(request, 'tasks/project_form.html', {'form': form})

# FBV (Function Based View)
def home_view(request):
    return render(request, "tasks/index.html")


def project_list_view(request):
    projets = ProjectService.get_user_projects(request.user)
    return render(request, "tasks/project_list.html", {"projets": projets})

def delete_project_view(request, project_id):
    user = request.user
    try:
        ProjectService.delete_project(project_id, user)
    except PermissionDenied as e:
        messages.add_message(request, messages.ERROR, str(e))
        return redirect("tasks:list")
            
    messages.add_message(request, messages.SUCCESS, "Le projet a été supprimé avec succès")
    return redirect("tasks:list")

def project_detail_view(request, project_id):
    user = request.user
    project = ProjectService.get_project(project_id, user)
    return render(request, "tasks/project_detail.html", {"project": project})