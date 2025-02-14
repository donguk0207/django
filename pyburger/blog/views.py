from django.shortcuts import render, redirect
from blog.models import Post, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment = request.POST["comment"]
        Comment.objects.create(
            post=post,
            content=comment,
        )
    return render(request, "post_detail.html", {"post": post})

def post_add(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
        )
        return redirect(f"/posts/{post.id}/")
    return render(request, "post_add.html")
