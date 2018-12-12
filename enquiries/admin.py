from django.contrib import admin
from .models import Enquiry
# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'phone', 'enquiry_date')
    list_display_links = ('id', 'name')
    list_per_page = 25
    search_fields = ('name', 'listing', 'email')

admin.site.register(Enquiry, EnquiryAdmin)