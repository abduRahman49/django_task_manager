from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import ProjectForm
from .services import ProjectService


# Create your views here.
class ProjectView(View):

    def post(self, request):
        # request.POST => contient les informations de l'utilisateur
        form = ProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            owner = request.user
            project = ProjectService.create_project(data.get("title"), owner)
            return HttpResponse(f"Le projet {project.title} a bien été créé")
            ## return redirect("tasks:list") # redirige vers une autre url après création du projet


    def get(self, request):
        form = ProjectForm()
        return render(request, 'tasks/project_form.html', {'form': form})


def home_view(request):
    return render(request, "tasks/index.html")
