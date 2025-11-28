from django.db import models
from django.contrib.auth.models import User

class Item_Lost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    item_name = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    date_lost = models.DateField()
    contact_number = models.CharField(max_length=15)
    date_posted = models.DateField(auto_now_add=True)

    photo = models.ImageField(upload_to='lost_items/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.item_name}"
