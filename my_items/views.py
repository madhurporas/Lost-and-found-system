from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from report_lost.models import Item_Lost
from report_found.models import Item_Found

@login_required
def my_items(request):
    user = request.user

    total_lost = Item_Lost.objects.filter(user=user).count()
    total_found = Item_Found.objects.filter(user=user).count()

    # Since no status field exists in models, set default values
    returned_items = 0
    active_claims = 0

    lost_items = Item_Lost.objects.filter(user=user).order_by("-id")
    found_items = Item_Found.objects.filter(user=user).order_by("-id")

    # Add temporary status field
    for item in lost_items:
        item.status = "lost"

    for item in found_items:
        item.status = "found"

    context = {
        "total_lost": total_lost,
        "total_found": total_found,
        "returned_items": returned_items,
        "active_claims": active_claims,
        "lost_items": lost_items,
        "found_items": found_items,
    }

    return render(request, "my_items/my_items.html", context)
