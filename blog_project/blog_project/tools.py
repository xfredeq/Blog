from datetime import date

from blog.models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404


def get_all_posts():
    fetched_posts = Post.objects.all().order_by('-date')
    return fetched_posts


def get_latest_posts():
    return get_all_posts()[:2]


def get_specific_post(slug) -> Post:
    return get_object_or_404(Post, slug=slug)
