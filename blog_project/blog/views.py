from django.views import View
from django.shortcuts import render
from blog_project.tools import get_all_posts, get_specific_post
# Create your views here.


class PostView(View):
    def get(self, request, slug=None):
        if slug is None:
            return render(request, 'blog/all_posts.html', context={
                "posts": get_all_posts()
            })
        return render(request, 'blog/single_post.html', context={
            'post': get_specific_post(slug)
        })
