from django.urls import path

from .views import (
    ContactsView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductsListView,
    ProductUpdateView,
)

app_name = "catalog"

urlpatterns = [
    path("home/", ProductsListView.as_view(), name="products_list"),
    path("home/new", ProductCreateView.as_view(), name="product_create"),
    path("home/<int:pk>", ProductDetailView.as_view(), name="product_info"),
    path("home/update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("home/delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]
