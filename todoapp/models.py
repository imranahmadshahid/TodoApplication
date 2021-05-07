from django.db import models
from django.contrib.auth.models import User

class TodoModel(models.Model):
    description = models.CharField(max_length = 180)
    isDone = models.BooleanField(default = False, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.description