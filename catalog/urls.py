from django.urls import path

from .views import (
    CategoryProductsView,
    ContactsView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductsListView,
    ProductUnpublishView,
    ProductUpdateView,
)

app_name = "catalog"

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path(
        "<int:pk>/unpublish/", ProductUnpublishView.as_view(), name="product_unpublish"
    ),
    path(
        "category/<int:category_id>/",
        CategoryProductsView.as_view(),
        name="category_products",
    ),
]
