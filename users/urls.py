from django.urls import path, include

from users import views

app_name = "users"

urlpatterns = [
    path("", views.Users.as_view(), name="list"),
    path("create/", views.Create.as_view(), name="create"),
]
