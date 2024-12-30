from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    recent_posts = [
        {'title': 'Post 1', 'content': 'Content for post 1'},
        {'title': 'Post 2', 'content': 'Content for post 2'},
        {'title': 'Post 3', 'content': 'Content for post 3'},
    ]
    return render(request, 'blog/home.html', {'recent_posts': recent_posts})


