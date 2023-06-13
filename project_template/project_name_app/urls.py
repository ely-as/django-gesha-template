from django.urls import path

from {{ project_name }}_app import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("enquiry/", views.EnquiryView.as_view(), name="enquiry"),
]
