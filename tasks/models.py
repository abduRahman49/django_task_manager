from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(User):
    pass


class Project(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Task(models.Model):

    class Status(models.TextChoices):
        TODO = "TODO"
        IN_PROGRESS = "IN_PROGRESS"
        DONE = "DONE"

    title = models.CharField(max_length=200)
    description = models.CharField(null=True)
    status = models.CharField(choices=Status.choices, default=Status.TODO)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, null=True, on_delete=models.DO_NOTHING)

    def update_status(self, status):
        if not status in Task.Status.values:
            raise ValueError("Statut invalide")

        self.status = status
        self.save(update_fields=["status"])
