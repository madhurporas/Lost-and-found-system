from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from report_lost.models import Item_Lost
from report_found.models import Item_Found
from notifications.models import Notification
#login page for project
@login_required
def home(request):

    lost_items = Item_Lost.objects.all().order_by("-id")
    found_items = Item_Found.objects.all().order_by("-id")
    unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
    # Tag each object
    for item in lost_items:
        item.status = "lost"

    for item in found_items:
        item.status = "found"
        item.date_lost = item.date_found  # unify field name

    # Merge both lists
    all_items = list(lost_items) + list(found_items)

    # Sort by id (newest first)
    all_items = sorted(all_items, key=lambda x: x.id, reverse=True)

    return render(request, "home/home.html", {
        "items": all_items,
        "unread_count": unread_count,
    })
