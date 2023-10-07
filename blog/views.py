from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'simon',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 28, 2023'
    },
    {
        'author': 'Kofi',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})