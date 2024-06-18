from django.shortcuts import render
from .models import Product
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            search = request.GET.get("search")
            if not search:
                products = Product.objects.all()
                context = {
                    "products": products,
                    "search": search,
                }
                return render(request, "main/shop.html", context)
            else:
                products = Product.objects.filter(name__icontains=search)
                if products:
                    context = {
                        "products": products,
                        "search": search,
                    }
                    return render(request, "main/shop.html", context)
                else:
                    return render(request, "main/404.html")


class ProductDetailView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "main/cart.html")


class CheckoutPageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "main/checkout.html")


