from django.shortcuts import render, redirect, get_object_or_404
from notifications.models import Notification
from report_lost.models import Item_Lost
from report_found.models import Item_Found

def cont_looser(request, id):

    # GET LOST ITEM (not found item)
    lost = get_object_or_404(Item_Lost, id=id)

    if request.method == "POST":
        finder_message = request.POST.get("finder_message", "")
        Notification.objects.create(
            user=lost.user,
            finder=request.user,        # lost item ka owner
            notif_type="match",
            title=f"Someone Found Your Item! '{lost.item_name}'",
            message=f"This User says they found something similar to '{lost.item_name}'. Please verify the details by reaching out to {request.user.profile_making.first_name}.",
            message_from_finder=finder_message,
            related_item_id=lost.id
        )

        return redirect("notifications")  

    return render(request, "contact_looser/contact_looser.html", {
        "lost": lost
    })
