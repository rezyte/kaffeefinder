from django.urls import path

from . import views

app_name = "cafes"

urlpatterns = [
    path("", views.CafeListView.as_view(), name="list"),
    path("my/", views.MyCafesView.as_view(), name="my-cafes"),
    path("add/", views.CafeCreatView.as_view(), name="add_cafe"),
    path("<str:slug>/", views.SingleCafeView.as_view(), name="single-cafe"),
    path("<str:slug>/edit/", views.CafeUpdateView.as_view(), name="cafe-update"),

]
