from django.urls import path
from . import views

urlpatterns = [
    path("fbv_template_view", views.my_template_view, name="fbv_template"),
    path("cbv_template_view",views.MyTemplateView.as_view(), name="cbv_template"),
]
