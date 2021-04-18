from django.shortcuts import render


def register(request):
    return render(request, "registration/register.html")


def users(request):
    return render(request, "registration/users.html")
