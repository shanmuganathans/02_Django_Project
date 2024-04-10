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
    path("fbv_detail_view/<int:id>",views.fbv_detail_view, name ="fbv_detail_view"),
    path("cbv_detail_view/<int:pk>",views.CBVDetailView.as_view(), name="cbv_detail_view"),
    path("fbv_update_view/<int:id>",views.fbv_update_view, name="fbv_update_view"),
    path("cbv_update_view/<int:id>",views.CBVUpdateView.as_view(), name="cbv_update_view"),
    path("fbv_delete_view/<int:id>",views.fbv_delete_view, name="fbv_delete_view"),
    path("cbv_delete_view/<int:id>",views.CBVDeleteView.as_view(), name="cbv_delete_view"),
]
