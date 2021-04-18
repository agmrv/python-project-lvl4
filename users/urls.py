from django.urls import path, include

from users import views


app_name = "users"

urlpatterns = [
    path("", views.users, name="users"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]
