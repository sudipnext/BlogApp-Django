from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required(login_url="/authentication/login/")
def index(request):
    blogs = Post.objects.filter(user=request.user)
    context={
        'blogs': blogs
    }

    return render(request, "myblog/index.html", context)

def add_post(request):
    if request.method == 'GET':
        return render(request, "myblog/index.html")
    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        Post.objects.create(title=title, description=description, user=request.user)
        return redirect('home')
