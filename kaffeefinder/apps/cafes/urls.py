from django.urls import path

from . import views

app_name = "cafes"

urlpatterns = [
    path("add/", views.CafeCreatView.as_view(), name="add_cafe"),
    path("<str:slug>/", views.SingleCafeView.as_view(), name="single-cafe"),
]
