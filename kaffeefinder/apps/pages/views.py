from django.views import View, generic

class IndexView(generic.TemplateView):
    template_name = "index.html"
    
