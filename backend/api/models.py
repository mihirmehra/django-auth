from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)                                       
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)                                  # automaticaly automate
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note")       # the foreign key helps to can link the user with some data that belong to that user
    
    def __str__(self):
        return self.title
    