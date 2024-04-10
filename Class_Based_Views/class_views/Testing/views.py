from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
    template_name = "Testing/list_template_class_based.html"
    queryset =  Contact.objects.all()
    context_object_name = "contacts"


def fbv_detail_view(request, id):
    try:
        obj = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        return HttpResponse("Contact not found.!")
    context = {"contact": obj}
    return render(request,"Testing/detail_view.html", context)


class CBVDetailView(DetailView):
    template_name = "Testing/detail_view.html"
    pk_url_kwarg = 'pk'
    queryset = Contact.objects.all()
    
def fbv_update_view(request, id):
    obj = get_object_or_404(Contact, id =id)
    if request.method =="GET":
        context = {
            "form":ContactForm(instance=obj)
        }
        return render(request,"Testing/form_update.html", context)
    elif request.method =="POST":
        form = ContactForm(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect("cbv_list_view")
        else:
            return render(request, "Testing/form_update.html",context)
        
        
class CBVUpdateView(UpdateView):
    template_name = "Testing/form_update.html"
    form_class = ContactForm
    pk_url_kwarg = "id"
    model = Contact
    
    def form_valid(self, form):
        form.save()
        return redirect("cbv_list_view")
    
def fbv_delete_view(request, id):
    object = get_object_or_404(Contact, id =id)
    if request.method =="GET":
        context = {"contact": object}
        return render(request, "Testing/delete_template.html", context)
    if request.method == "POST":
        object.delete()
        return HttpResponse("Contact deleted successfully..!")
    
    
class CBVDeleteView(DeleteView):
    template_name = "Testing/delete_template.html"
    pk_url_kwarg = "id"
    queryset = Contact.objects.all()
    
    def form_valid(self, form):
        self.object = self.get_object()
        self.object.delete()
        return redirect("cbv_list_view")