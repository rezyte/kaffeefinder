from django import forms

from .models import Review

class CommentForm(forms.ModelForm):

	class Meta:
		model = Review
		fields = ("cafe", "image", "user", "content",)