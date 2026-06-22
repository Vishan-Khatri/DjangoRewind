from django.contrib import admin
from .models import Listing, ContactMessage

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display  = ['title', 'city', 'rent', 'room_type', 'owner', 'is_active', 'created_at']
    list_filter   = ['city', 'room_type', 'gender_pref', 'is_active', 'furnished', 'wifi']
    search_fields = ['title', 'address', 'owner__username']
    list_editable = ['is_active']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'listing', 'is_read', 'created_at']
    list_filter  = ['is_read']
