from django.urls import path
from . import views
urlpatterns = [
    path("", views.IndexPageListView.as_view(), name="index"),
    path("about/", views.AboutPageListView.as_view(), name="about"),
]