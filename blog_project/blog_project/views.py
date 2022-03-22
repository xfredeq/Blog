from django.views import View
from django.shortcuts import render
from blog_project.tools import get_latest_posts


class MainView(View):
    def get(self, request):
        return render(request, "index.html", context={
            "posts": get_latest_posts()
        })
