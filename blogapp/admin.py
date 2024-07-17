from django.contrib import admin
from .models import BlogPost
# Register your models here.

admin.site.site_header = 'Blog App'
admin.site.site_title = 'title'
admin.site.index_title = 'Blog Neccessery Fields'

class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ['author', 'title', 'text']
    
    #this setting for admin doesn't let admin to change users posts
admin.site.register(BlogPost, BlogPostAdmin)

# class Postcomment(admin.StackedInline):
#     model = PostComment
#     extra = 1

# class BlogPostAdmin(admin.ModelAdmin):
    
#     list_display = [
#         'author',
#         'title',
#         'date',
#     ]
#     inlines = [Postcomment]
#     search_fields = ['author', 'title'] #adds search bar in django admin 
#     #panel to search toward database
#     list_filter = [ #filters lists in right side inside a box 
#         'date',
    # ]
# admin.site.register(PostComment)
# admin.site.register(BlogPost, BlogPostAdmin)


