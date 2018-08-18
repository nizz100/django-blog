from django.contrib import admin

# Register your models here.
from App.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category','pub_time']



admin.site.register(Blog, BlogAdmin)