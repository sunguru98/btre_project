from django.urls import path
from . import views
urlpatterns = [
    path("", views.IndexPageTemplateView.as_view(), name="home"),
    path("about/", views.AboutPageTemplateView.as_view(), name="about"),
]