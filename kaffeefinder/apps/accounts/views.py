from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .forms import CafeManagerCreationForm

from kaffeefinder.apps.core.mixins import AnonymousMixin

class SignUpView(AnonymousMixin, generic.FormView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginView(AnonymousMixin, generic.FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

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


class LogoutView(View):

    def get(self, request):
        if self.request.is_authenticated:
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
