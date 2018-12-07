from django.urls import path
from . import views

app_name = "listings"

urlpatterns = [
    path("", views.ListingPageListView.as_view(), name="listings_index"),
    path("<int:pk>/", views.ListingPageDetailView.as_view(), name="listing_detail"),
    path("search/", views.ListingSearchTemplateView.as_view(), name="search"),
]