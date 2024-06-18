from django.shortcuts import render
from .models import BlogPost
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogPageView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            search = request.GET.get("search")
            if not search:
                posts = BlogPost.objects.all()
                context = {
                    "posts": posts,
                    "search": search,
                }
                return render(request, "main/blog.html", context)
            else:
                posts = BlogPost.objects.filter(title__icontains=search)
                if posts:
                    context = {
                        "posts": posts,
                        "search": search,
                    }
                    return render(request, "main/blog.html", context)
                else:
                    return render(request, "main/404.html")

