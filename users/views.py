from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from profile_making.models import Profile_Making

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            profile, created = Profile_Making.objects.get_or_create(user=user, defaults={
                'email_address': user.email,
                # you can set sensible defaults for required fields:
                'phone_number': 0,
                'first_name': user.first_name or '',
                'last_name': '',
            })
            messages.success(request, "Logged in successfully!")
            if profile.is_profile_completed:
                return redirect('Home')
            else:
                return redirect("Make_Profile")
            
            
        else:
            messages.error(request, "Invalid email or password!")
            return redirect("Login")
    return render(request,'users/login.html')
def register(request):
    if request.method == 'POST':
        # fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        # phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("Register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists!")
            return redirect("Register")
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            # first_name=fullname
        )
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect("Login")

    return render(request,'users/register.html')

def logout_user(request):
    logout(request) 
    return redirect('LandingPage')  
