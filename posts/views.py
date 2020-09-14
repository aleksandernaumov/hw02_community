from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    latest = Post.posts_list()[:11]
    return render(request, 'index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.posts_list(group)[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})
