from django.shortcuts import render
from report_lost.models import Item_Lost
from report_found.models import Item_Found
def view_profile_info(request):
    user = request.user

    total_lost = Item_Lost.objects.filter(user=user).count()
    total_found = Item_Found.objects.filter(user=user).count()
    context = {
        'total_lost':total_lost,
        'total_found':total_found,
    }
    return render(request, 'view_profile/profile_info.html', context)



