from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from staff.models import Staff

class AboutPageView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            search = request.GET.get("search")
            if not search:
                staffs = Staff.objects.all()
                context = {
                    "staffs": staffs,
                    "search": search,
                }
                return render(request, "main/about.html", context)
            else:
                staffs = Staff.objects.filter(position__icontains=search)
                if staffs:
                    context = {
                        "staffs": staffs,
                        "search": search,
                    }
                    return render(request, "main/about.html", context)
                else:
                    return render(request, "main/404.html")
