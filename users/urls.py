from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CustomLoginView, RegisterView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        CustomLoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/", LogoutView.as_view(next_page="catalog:products_list"), name="logout"
    ),
]
