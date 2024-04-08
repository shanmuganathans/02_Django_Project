from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post

from .forms import PostForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    # title ="welcome to django class"
    posts = Post.objects.all()
    context = {
        # "title": title,
        "posts": posts,
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html")


@login_required
def create_post(request):
    if request.method == "GET":
        context = {
            "form": PostForm()
        }
        return render(request,"blog/post_form.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The post has been created successfully..!")
            return redirect("posts")
        else:
            messages.error(request,"Please correct the following error:")
            return render(request,"blog/post_form.html", context={"form": form})
        
@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id = id)
    
    if request.method == "GET":
        context = {"form":PostForm(instance=post), "id":id}
        return render(request, "blog/post_form.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "The post has been Editied successfully..!")
            return redirect("posts")
        else:
            messages.error(request,"Please correct the following error:")
            return render(request, "blog/post_form.html", context={"form":form})
        
@login_required      
def delete_post(request, pk):
    post = get_object_or_404(Post, id =pk)
    context = {"post":post}
    
    if request.method =="GET":
        return render(request, "blog/post_confirm_delete.html", context)
    elif request.method == "POST":
        post.delete()
        messages.success(request, "The post has been deleted successfully..!" )
        return redirect("posts")
        