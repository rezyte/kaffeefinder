from django.urls import path

from . import views

app_name = "comments"


urlpatterns = [
	path("add/<str:slug>/", views.CreateCommentView.as_view(), name="add-comment"),
]