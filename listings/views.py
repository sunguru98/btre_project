from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class ListingPageListView(TemplateView):
    template_name = "listings/listings.html"
    #context_object_name = "listings"

class ListingPageDetailView(DetailView):
    template_name = "listings/listing.html"

class ListingSearchTemplateView(TemplateView):
    template_name = "lisitngs/search.html"