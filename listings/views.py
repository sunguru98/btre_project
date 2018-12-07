from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Listing
# Create your views here.
class ListingPageListView(ListView):
    model = Listing
    template_name = "listings/listings.html"
    context_object_name = "listings"

class ListingPageDetailView(DetailView):
    model = Listing
    context_object_name = "listing"
    template_name = "listings/listing.html"

class ListingSearchTemplateView(TemplateView):
    template_name = "lisitngs/search.html"