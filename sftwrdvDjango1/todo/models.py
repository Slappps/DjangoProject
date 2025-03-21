from django.db import models

# Create your models here.
class TodoItem(models.Model):
    todo_text = models.CharField(max_length=200)
    due_date = models.DateTimeField("date published")
    completed = models.BooleanField(default=False)