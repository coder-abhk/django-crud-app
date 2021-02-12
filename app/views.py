from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm


def app_view(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)


def create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "create.html", {"form": form})


def update_view(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)
    return render(request, "update.html", {"form": form})


def delete_view(request, pk):
    if(Post.objects.get(id=pk)):
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("home")
