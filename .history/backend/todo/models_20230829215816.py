from django.db import models

class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.CharField