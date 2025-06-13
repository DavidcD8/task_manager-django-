from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name