from django.shortcuts import render, redirect, get_object_or_404
from notifications.models import Notification
from report_lost.models import Item_Lost
from report_found.models import Item_Found

def cont_finder(request, id):

    # GET LOST ITEM (not found item)
    found = get_object_or_404(Item_Found, id=id)

    if request.method == "POST":
        owner_message = request.POST.get("owner_message", "")
        Notification.objects.create(
            user=found.user,
            owner=request.user,        # lost item ka owner
            notif_type="match",
            title=f"Owner Found for '{found.item_name}'",
            message=f"This User says that the item you found is similar to their lost item. Please verify the details by reaching out to {request.user.profile_making.first_name}.",
            message_from_owner=owner_message,
            related_item_id=found.id
        )

        return redirect("notifications")  

    return render(request, 'contact_finder/contact_finder.html', {
        "found": found
    })

    