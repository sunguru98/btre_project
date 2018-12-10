from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from listings.choices import state_choices, bedroom_choices, price_choices
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listing
# Create your views here.
class ListingPageListView(ListView):
    queryset = Listing.objects.order_by('-published_date').filter(is_published=True)
    template_name = "listings/listings.html"
    context_object_name = "listings"
    paginate_by = 6


class ListingPageDetailView(DetailView):
    model = Listing
    context_object_name = "listing"
    template_name = "listings/listing.html"

# class ListingSearchTemplateView(TemplateView):
#     template_name = "listings/search.html"

def search(request):
    listings = Listing.objects.order_by("-published_date").filter(is_published=True)

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            listings = listings.filter(description__icontains=keywords)
    
    #City
    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            listings = listings.filter(city__iexact=city)

    #State
    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            listings = listings.filter(state__iexact=state)

    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            listings = listings.filter(bedrooms__iexact =bedrooms)

    #Price
    if 'price' in request.GET:
        price = request.GET.get('price')
        if price:
            listings = listings.filter(price__lte=price)
    
    page = request.GET.get('page',1)
    paginator = Paginator(listings, 6)
    
    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    context = {
        'price_choices':price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': listings,
        'values': request.GET
    }
    return render(request, "listings/search.html", context)