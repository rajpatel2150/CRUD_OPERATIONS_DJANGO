# Creating a model for the app

from django.db import models

# class based model which contains tasks

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):              # representing only the title 
        return self.title