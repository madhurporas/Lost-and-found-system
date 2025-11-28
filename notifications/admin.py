from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'finder', 'owner', 'notif_type', 'title','message', 'message_from_finder', 'message_from_owner','related_item_id','is_read','created_at')