from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item_Found
from datetime import date
from notifications.models import Notification
@login_required
def report_found(request):

    if request.method == "POST":
        
        item_name = request.POST.get("item_name")
        category = request.POST.get("category")
        description = request.POST.get("description")
        color = request.POST.get("color")
        location = request.POST.get("location")
        date_found = request.POST.get("date_found")
        contact_number = request.POST.get("contact_number")
        condition=request.POST.get("condition")
        photo = request.FILES.get("photo")   # file handling

        found_item = Item_Found(
            user = request.user,
            item_name = item_name,
            category = category,
            description = description,
            color = color,
            location = location,
            date_found = date_found,
            contact_number = contact_number,
            photo = photo,
            condition=condition
        )

        found_item.save()

        
        Notification.objects.create(
            user=request.user,
            notif_type="update",
            title="Found Item Reported",
            message=f"Your item '{found_item.item_name}' was reported successfully.",
            related_item_id=found_item.id
        )
        return redirect("Home")  # redirect anywhere after save
    context = {
        "today": date.today().isoformat()
    }

    return render(request, 'report_found/report_found.html', context)
