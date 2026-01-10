from django import forms


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=200)

