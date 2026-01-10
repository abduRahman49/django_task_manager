from django.shortcuts import render
from django.views import View
from .forms import ProjectForm


# Create your views here.
class ProjectView(View):

    def post(self, request):
        # request.POST => contient les informations de l'utilisateur
        pass

    def get(self, request):
        form = ProjectForm()
        return render(request, 'tasks/project_form.html', {'form': form})
