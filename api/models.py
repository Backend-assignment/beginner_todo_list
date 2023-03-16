from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=20)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
    
# Kill the port 8000
# sudo kill -9 $(sudo lsof -t -i:8000)