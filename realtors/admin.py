from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'email', 'phone', 'hired_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone', 'email', 'hired_date')

admin.site.register(Realtor, RealtorAdmin)