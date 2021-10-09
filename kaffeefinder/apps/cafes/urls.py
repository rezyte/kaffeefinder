from django.urls import path

from . import views

app_name = "cafes"

urlpatterns = [
    path("", views.CafeListView.as_view(), name="list"),
    path("add/", views.CafeCreatView.as_view(), name="add_cafe"),
    path("<str:slug>/", views.SingleCafeView.as_view(), name="single-cafe"),
]
