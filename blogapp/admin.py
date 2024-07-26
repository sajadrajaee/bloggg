from django.contrib import admin
from users.models import CustomUsers
from .models import BlogPost, Comment, Categories
# Register your models here.

admin.site.site_header = 'Blog App'
admin.site.site_title = 'title'
admin.site.index_title = 'Blog Neccessery Fields'

class BlogPostAdmin(admin.ModelAdmin):
    author = BlogPost.author
    readonly_fields = []
    
    
    #this setting for admin doesn't let admin to change users posts
admin.site.register(BlogPost, BlogPostAdmin)
# admin.site.register(Comment)
admin.site.register(Categories)


