from django.db import models
from django.utils import timezone
from users.models import CustomUsers
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        CustomUsers, max_length=100, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    images = models.ImageField(upload_to='blogapp/images', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"