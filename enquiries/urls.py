from django.urls import path
from . import views

app_name = "enquiries"
urlpatterns = [
    path("enquiry/", views.enquiry, name="enquiry")
]