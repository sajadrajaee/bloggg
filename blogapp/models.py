from django.db import models
from django.utils import timezone
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    images = models.ImageField(upload_to='static/images')

    def __str__(self):
        return f"{self.title} - {self.author}"