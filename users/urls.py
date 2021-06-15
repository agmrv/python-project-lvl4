from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("", views.List.as_view(), name="list"),
    path("create/", views.Create.as_view(), name="create"),
    path("<int:user_id>/update/", views.Update.as_view(), name="update"),
    path("<int:user_id>/delete/", views.Delete.as_view(), name="delete"),
]
