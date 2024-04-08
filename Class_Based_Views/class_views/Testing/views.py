from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def my_template_view(request):
    context = {"title": "Simple template view testing"}
    return render(request, "Testing/template_view.html", context)


class MyTemplateView(TemplateView):
    template_name = "Testing/template_view.html"
    
    def get_context_data(self):
        context = {"title": "Class based: Simple template view  "}
        return context
    