from django.db import models
from django.utils import timezone
from users.models import CustomUsers
from multiupload.fields import MultiImageField
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        CustomUsers, max_length=100, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    images = models.ImageField( null=True, blank=True)
    like = models.ManyToManyField(CustomUsers, related_name = 'post_like')

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def number_of_likes(self):
        return self.like.count()
    
    
# class Image(models.Model):
#     image = models.ForeignKey(BlogPost, on_delete= models.CASCADE)