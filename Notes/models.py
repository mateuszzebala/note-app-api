from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=16)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
    
    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
        }