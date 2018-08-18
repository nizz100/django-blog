from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from App.models import Blog


def Test(request):
    # post = Blog.objects.all()
    return render(request, 'blog/test.html',{'current_time':datetime.now()})


def home(request):
    post_list = Blog.objects.all()
    return render(request, 'blog/home.html',{'post_list':post_list})


def Detail(request,id):
    try:
        post = Blog.objects.get(id = id)
    except Blog.DoesNotExist:
        return Http404
    return render(request, 'blog/post.html', {'post':post})


def index(request):
    pass