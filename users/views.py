from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class Create(View):
    template_name = "registration/create.html"

    def get(self, request):
        return render(request, self.template_name, context={"form": UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")


class Update(LoginRequiredMixin, View):
    login_url = "login"
    template_name = "users/update.html"

    def handle_no_permission(self):
        return redirect(self.login_url)

    def get(self, request, user_id):
        context = {"username": User.objects.get(id=user_id).username}
        return render(request, self.template_name, context=context)


class Delete(LoginRequiredMixin, View):
    login_url = "login"
    template_name = "users/delete.html"

    def handle_no_permission(self):
        return redirect(self.login_url)

    def get(self, request, user_id):
        context = {"user": User.objects.get(id=user_id)}
        return render(request, self.template_name, context=context)

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect("tasks:index")


class Users(View):
    template_name = "users/users_list.html"

    def get(self, request):
        users = User.objects.all()
        context = {"users": users}
        return render(request, self.template_name, context=context)
