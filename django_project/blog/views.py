from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    "author":"Harish Kumar",
    "title":"Blog Post 1",
    "content":"first post content",
    "created_at":"Oct 30, 2022"
    },
    {
    "author":"Harish Kumar sa",
    "title":"Blog Post 2",
    "content":"second post content",
    "created_at":"Oct 30, 2022"
    }
    ]

# Create your views here.
def home(request):
    context = {
        "posts": posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')