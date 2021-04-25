from django.shortcuts import render
from django.views import View


class Register(View):
    template_name = "registration/register.html"

    def get(self, request):
        return render(request, self.template_name)


class Users(View):
    template_name = "registration/users.html"

    def get(self, request):
        return render(request, self.template_name)
