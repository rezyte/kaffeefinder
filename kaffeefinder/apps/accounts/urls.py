from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.NewLoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("sup_signup/", views.SignUpAsCafeManager.as_view(), name="signup_as_manager"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
