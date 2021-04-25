from django.urls import path, include

from users import views


app_name = "users"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", views.Users.as_view(), name="users"),
    path("register/", views.Register.as_view(), name="register"),
]
