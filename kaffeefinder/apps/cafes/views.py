from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.http import HttpResponse
from django.contrib.auth import mixins
from django.contrib import messages

from .models import Cafe
from .forms import CafeForm

class CafeCreatView(mixins.LoginRequiredMixin, View):

    def get(self, request):
        form = CafeForm()
        return render(request, "cafes/create.html", context={"form": form})

    def post(self, request):
        data = request.POST.copy()
        print(request.user)
        data.update({"owner": request.user})
        print(data)
        form = CafeForm(data, request.FILES)
        if form.is_valid():
            cafe = form.save()
            messages.success(request, "شما کافه خود را با موفقیت ایجاد کردید")
            return redirect(
                reverse("cafe:single-cafe", kwargs={"slug": cafe.slug})
            )
        else:
            print(form.errors)
            return HttpResponse(form.errors, "<br><a href="/cafes/add/">Go Back</a>")

class SingleCafeView(generic.DetailView):
    template_name = "cafes/detail.html"
    queryset = Cafe.objects.all()
    slug = "slug"

class CafeListView(generic.ListView):
    template_name = "cafes/list.html"
    queryset = Cafe.objects.all()
