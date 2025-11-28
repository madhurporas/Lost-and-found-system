from django.db import models
from django.contrib.auth.models import User 
class Profile_Making(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    email_address=models.EmailField()
    phone_number=models.IntegerField()
    enrolment_id=models.CharField(max_length=20, default="")
    first_name=models.CharField(max_length=20, default="")
    last_name=models.CharField(max_length=20, default="")
    college_name=models.CharField(max_length=30, default="")
    department=models.CharField(max_length=15, default="")
    year=models.CharField(max_length=15, default="")
    campus_address=models.CharField(max_length=30, default="")
    bio=models.TextField(default="")
    is_profile_completed=models.BooleanField(default=False)

    profile_image=models.ImageField(upload_to='profile_images/',default='default/user.png')

    def __str__(self):
        return self.user.username
