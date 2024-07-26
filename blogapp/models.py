from django.db import models
from users.models import CustomUsers
# Create your models here.

class Categories(models.Model):
    category = models.CharField(
        max_length=150,
        default=None,
        null=True
    )

    def __str__(self):
        return self.category

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        CustomUsers, max_length=100, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    cate_gory = models.ForeignKey(
        Categories, on_delete=models.CASCADE, 
        help_text="must be selected from existing options",
        default=None,
        null=True
    )
    
    images = models.ImageField( null=True, blank=True)
    # like = models.ManyToManyField(CustomUsers, related_name = 'post_like')

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def number_of_likes(self):
        return self.like.count()

class Comment(models.Model): #charfield for comment, how to set foriegn key 
    author = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.CharField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return "{}|{}".format(self.author, self.comment[:20])