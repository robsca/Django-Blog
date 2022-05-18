from django.shortcuts import render

# Create your views here.
# app/Blog/views.py

from django.shortcuts import render
from .models import Article
# Create your views here.

# views

def all_post(request):
    articles = Article.objects.all()
    return render(request, 'Blog/all_post.html', {'articles' : articles})

def post_detail(request, auto_increment_id):
    article = Article.objects.get(auto_increment_id=auto_increment_id)
    return render(request, 'Blog/post_detail.html', {'article' : article})

def home(request):
    return render(request, 'Blog/base.html')