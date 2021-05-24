from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View


class Create(View):
    template_name = "registration/create.html"

    def get(self, request):
        return render(request, self.template_name)


class Users(View):
    template_name = "users/users_list.html"

    def get(self, request):
        users = User.objects.all()
        context = {"users": users}
        return render(request, self.template_name, context=context)
