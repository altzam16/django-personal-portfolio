from django.shortcuts import render, get_object_or_404
from .models import Post


def all_blogs(request):
    post_count = Post.objects.all()
    posts = Post.objects.order_by('-ex_date')[:5]
    return render(request, 'blog/all_blogs.html',{'posts':posts, 'pc':post_count})

def detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request, 'blog/detail.html',{'post':post})