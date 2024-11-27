from django.db import models


class Task(models.Model):
    title_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    completed = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    def str(self):
        return f'{self.title_name}, {self.description}, {self.completed}, {self.created_date}'
