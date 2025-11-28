from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile_Making
from django.contrib.auth.models import User
@login_required
def make_profile(request):
    if request.method == 'POST':

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        college_name = request.POST.get("college_name")
        enrolment = request.POST.get("enrolment")
        department = request.POST.get("department")
        year = request.POST.get("year")
        phone_number = request.POST.get("phone_number")
        campus_address=request.POST.get("campus_address")
        bio=request.POST.get("bio")
        profile_image = request.FILES.get("profile_image")
        profile, created = Profile_Making.objects.get_or_create(
            user=request.user,
            defaults={
                'phone_number': phone_number or 0,
                'email_address': request.user.email,
                'enrolment_id': enrolment or '',
                'first_name': first_name or '',
                'last_name': last_name or '',
                'college_name': college_name or '',
                'department': department or '',
                'year': year or '',
                'campus_address': campus_address or '',
                'bio': bio or '',
                'profile_image': profile_image,
            }
        )

        if not created:
            profile.phone_number = phone_number or profile.phone_number
            profile.enrolment_id = enrolment or profile.enrolment_id
            profile.first_name = first_name or profile.first_name
            profile.last_name = last_name or profile.last_name
            profile.college_name = college_name or profile.college_name
            profile.department = department or profile.department
            profile.year = year or profile.year
            profile.campus_address = campus_address or profile.campus_address
            profile.bio = bio or profile.bio
            if profile_image:       # Only update if new file uploaded
                profile.profile_image = profile_image
        profile.is_profile_completed = True
        profile.save()
        return redirect('Home')
    return render(request, 'profile_making/profile.html')
