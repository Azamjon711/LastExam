from django.urls import path
from .views import ProductListView, ProductDetailView, CheckoutPageView

urlpatterns = [
    path("products/", ProductListView.as_view(), name='product'),
    path("product/detail/", ProductDetailView.as_view(), name='product-detail'),
    path("product/detail/checkout/", CheckoutPageView.as_view(), name='checkout'),

]
