from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.

class IndexPageListView(ListView):
    template_name = "pages/index.html"
    queryset = Listing.objects.order_by("-published_date").filter(is_published=True)[:3]
    context_object_name = "listings"


class AboutPageListView(ListView):
    template_name = "pages/about.html"
    model = Realtor
    
    def get_context_data(self, *args, **kwargs):
        context = super(AboutPageListView, self).get_context_data(*args, **kwargs)
        context['mvp_realtors'] = Realtor.objects.all().filter(is_mvp=True)
        return context

    context_object_name = "realtors"