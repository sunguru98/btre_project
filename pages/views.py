from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class IndexPageTemplateView(TemplateView):
    template_name = "pages/index.html"


class AboutPageTemplateView(TemplateView):
    template_name = "pages/about.html"