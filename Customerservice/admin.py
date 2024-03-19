# consumer_services/admin.py
from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['request_type', 'status', 'submitted_at', 'resolved_at']  # Display fields in the admin list view
    list_filter = ['status']  # Add filter options for status
    search_fields = ['request_type', 'details']  # Add search functionality
