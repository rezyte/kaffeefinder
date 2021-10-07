from django.contrib.auth.mixins import AccessMixin, UserPassesTestMixin
# from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from django.shortcuts import redirect

class AnonymousMixin(AccessMixin):

    def handle_no_permission(self):
        message = messages.warning(self.request, 'شما از پیش وارد سایت شده اید')
        return redirect("/")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)