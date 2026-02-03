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