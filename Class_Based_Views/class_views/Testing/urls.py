from django.urls import path
from . import views

urlpatterns = [
    path("fbv_template_view", views.my_template_view, name="fbv_template"),
    path("cbv_template_view",views.MyTemplateView.as_view(), name="cbv_template"),
    path("fbv_form_view", views.form_view_example, name="fbv_form_view"),
    path("cbv_form_view", views.FormViewExample.as_view(), name="cbv_form_view"),
    path("cbv_create_view", views.MyCreateView.as_view(), name="cbv_create_view"),
    path("fbv_list_view", views.fbv_list_view, name="fbv_list_view"),
    path("cbv_list_view", views.MyListView.as_view(), name="cbv_list_view"),
]
