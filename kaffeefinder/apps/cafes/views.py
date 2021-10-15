from django.shortcuts import render, redirect, reverse, get_object_or_404
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
                reverse("cafes:single-cafe", kwargs={"slug": cafe.slug})
            )
        else:
            print(form.errors)
            return HttpResponse(form.errors, "<br><a href="/cafes/add/">Go Back</a>")

class SingleCafeView(generic.DetailView):
    template_name = "cafes/detail.html"
    queryset = Cafe.objects.all()
    slug = "slug"

# class EditCafeView(View):

#     def get(self, request, slug):
#         cafe = get_object_or_404(Cafe, slug=slug)
#         return render(request, "cafes/create.html", context={ "instance": cafe })

#     def post(self, request, slug):
#         cafe = 


class MyCafesView(generic.ListView):
    template_name = "cafes/list.html"
    def get_queryset(self):
        return Cafe.objects.filter(owner=self.request.user)

class CafeUpdateView(generic.UpdateView):
    model = Cafe
    fields = ["title", "description", "slug", "image"]
    template_name = "cafes/create.html"

class CafeListView(generic.ListView):
    template_name = "cafes/list.html"
    queryset = Cafe.objects.all()
