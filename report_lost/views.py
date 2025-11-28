from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item_Lost
from datetime import date
from notifications.models import Notification
@login_required
def report_lost(request):

    if request.method == "POST":
        
        item_name = request.POST.get("item_name")
        category = request.POST.get("category")
        description = request.POST.get("description")
        color = request.POST.get("color")
        location = request.POST.get("location")
        date_lost = request.POST.get("date_lost")
        contact_number = request.POST.get("contact_number")

        photo = request.FILES.get("photo")   # file handling

        lost_item = Item_Lost(
            user = request.user,
            item_name = item_name,
            category = category,
            description = description,
            color = color,
            location = location,
            date_lost = date_lost,
            contact_number = contact_number,
            photo = photo
        )

        lost_item.save()

        
        Notification.objects.create(
            user=request.user,
            notif_type="update",
            title="Lost Item Reported",
            message=f"Your item '{lost_item.item_name}' was reported successfully.",
            related_item_id=lost_item.id
        )
        return redirect("Home")  # redirect anywhere after save
    context = {
        "today": date.today().isoformat()
    }

    return render(request, "report_lost/report_lost.html", context)
