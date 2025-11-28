from django.contrib import admin
from .models import Item_Found

@admin.register(Item_Found)
class FoundAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'item_name', 'category', 'description', 'color','location', 'date_found', 'contact_number','condition','photo')