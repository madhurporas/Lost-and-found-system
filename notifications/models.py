from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    NOTIF_TYPES = [
        ('match', 'Match'),
        ('message', 'Message'),
        ('update', 'Update'),
        ('alert', 'Alert'),
        ('success', 'Success'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # OWNER
    finder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="finder_user")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="owner_user")
    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPES)
    title = models.CharField(max_length=255)
    message = models.TextField()

    message_from_finder = models.TextField(null=True, blank=True)
    message_from_owner = models.TextField(null=True, blank=True)
    related_item_id = models.IntegerField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

