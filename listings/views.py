from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Listing
# Create your views here.
class ListingPageListView(ListView):
    queryset = Listing.objects.order_by('-published_date').filter(is_published=True)
    template_name = "listings/listings.html"
    context_object_name = "listings"
    paginate_by = 6
    #queryset = Listing.objects.all()

class ListingPageDetailView(DetailView):
    model = Listing
    context_object_name = "listing"
    template_name = "listings/listing.html"

class ListingSearchTemplateView(TemplateView):
    template_name = "lisitngs/search.html"