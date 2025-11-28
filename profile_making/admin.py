from django.contrib import admin
from .models import Profile_Making

@admin.register(Profile_Making)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'email_address', 'phone_number', 'enrolment_id', 'first_name','last_name', 'college_name', 'department','year','campus_address','bio','is_profile_completed','profile_image')