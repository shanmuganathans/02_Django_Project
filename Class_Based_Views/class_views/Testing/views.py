from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from . forms import ContactForm
from . models import Contact

# Create your views here.
def my_template_view(request):
    context = {"title": "Simple template view testing"}
    return render(request, "Testing/template_view.html", context)


class MyTemplateView(TemplateView):
    template_name = "Testing/template_view.html"
    
    def get_context_data(self):
        context = {"title": "Class based: Simple template view  "}
        return context

def form_view_example(request):
    if request.method =="GET":
        form = ContactForm()
        context = {"form":form}
        return render(request, "Testing/form_template.html",context)
    elif request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fbv_template")
        else:
            return render(request,"Testing/form_template.html", context={"form":form})
            
    

class FormViewExample(FormView):
    template_name = "Testing/form_template.html"
    form_class = ContactForm
    
    def form_valid(self, form):
        form.save()
        return redirect("cbv_template")
    

class MyCreateView(CreateView):
    template_name = "Testing/form_template.html"
    form_class = ContactForm
    
    def form_valid(self, form):
        form.save()
        return HttpResponse("Contact created successfully..!")
    
def fbv_list_view(request):
    contacts = Contact.objects.all()
    context = {"contacts": contacts}
    return render(request, "Testing/list_template.html",context)


class MyListView(ListView):
    template_name = "Testing/list_template.html"
    queryset =  Contact.objects.all()
    context_object_name = "contacts"