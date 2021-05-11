from django.urls import path, include

from users import views


app_name = "users"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("list/", views.Users.as_view(), name="list"),
    path("register/", views.Register.as_view(), name="register"),
]
