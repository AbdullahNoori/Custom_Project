from django.contrib import admin
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author', 'created', 'modified')

# Register your models here.
admin.site.register(Blog, BlogAdmin)