from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'published_date', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 25
    search_fields = ('title', 'address', 'city', 'state', 'zipcode', 'price')

admin.site.register(Listing, ListingAdmin)
