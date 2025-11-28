from django.contrib import admin
from .models import Item_Lost

@admin.register(Item_Lost)
class LostAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'item_name', 'category', 'description', 'color','location', 'date_lost', 'contact_number','photo')
