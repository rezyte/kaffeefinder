from django.shortcuts import render, redirect, reverse
from django.views import View, generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import CommentForm

class CreateCommentView(LoginRequiredMixin, View):

	def post(self, request, slug, *args, **kwargs):
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			print("\n"*3,"form is is_valid")
			form.save()
			messages.success(request, "شما با موفقیت  	نظر خود را ثبت کردید. ")
			return redirect(reverse("cafes:single-cafe", kwargs={"slug": slug}))
		else:
			print(form.errors)
			messages.success(request, "قرم نظر به درستی کامل نشده است")
			return redirect(reverse("cafes:single-cafe", kwargs={"slug": slug}))
