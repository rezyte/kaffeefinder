from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group


from .forms import CafeManagerCreationForm

from kaffeefinder.apps.core.mixins import AnonymousMixin


class SignUpView(AnonymousMixin, View):

    def get(self, request):
        return render(request, "accounts/signup.html")

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "شما با موفقیت جساب حور را ساختید")
            return redirect("cafes:list")
        else:
            print(form.errors)
            messages.error(request, form.errors)
            return redirect("accounts:signup")


class NewLoginView(LoginView):
     template_name = "accounts/login.html"


# a different view for cafe managers to sign up
# which redirects to a view to create their cafe
class SignUpAsCafeManager(AnonymousMixin, generic.FormView):
    template_name = "accounts/signup.html"
    form_class = CafeManagerCreationForm
    success_url = '/cafes/add/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class SignUpAsCafeManager(AnonymousMixin, View):

    def get(self, request):
        return render(request, "accounts/signup.html", context={"manager": True})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            mnger_gp, created = Group.objects.get_or_create(name="cafe manager") 
            mnger_gp.user_set.add(user)
            user.save()
            login(request, user)
            messages.success(request, "شما با موفقیت جساب حور را ساختید")
            return redirect("cafes:add_cafe")
        else:
            print(form.errors)
            messages.error(request, form.errors)
            return redirect("accounts:signup")

class LogoutView(View):

    def get(self, request):
        if self.request.user.is_authenticated:
            logout(request)
            messages.warning(request, "شما از حساب کاربری خود خارج شدید")
            return redirect("pages:index")
        else:
            messages.warning(request, "شما به این مسیر دسترسی ندارید")
            return redirect("pages:index")

    def post(self, request):
        if self.request.is_authenticated:
            logout(request)
            messages.warning(request, "شما از حساب کاربری خود خارج شدید")
            return redirect("pages:index")
        else:
            messages.warning(request, "شما به این مسیر دسترسی ندارید")
            return redirect("pages:index")
