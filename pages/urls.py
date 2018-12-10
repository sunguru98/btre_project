from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.AboutPageListView.as_view(), name="about"),
]