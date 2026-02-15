from django.contrib import admin
from .models import ContactMessage

# Register your model so it shows up in Django Admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # columns to display in admin list
    search_fields = ('name', 'email', 'message')    # optional: searchable fields
    list_filter = ('created_at',)                  # optional: filter by date