from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications_page(request):
    filter_type = request.GET.get("type", "all")

    qs = Notification.objects.filter(user=request.user)

    if filter_type == "unread":
        qs = qs.filter(is_read=False)
    elif filter_type in ["match", "message", "update", "alert", "success"]:
        qs = qs.filter(notif_type=filter_type)

    unread_count = Notification.objects.filter(user=request.user, is_read=False).count()

    return render(request, "notifications/notifications.html", {
        
        "notifications": qs.order_by("-created_at"),
        "unread_count": unread_count,
        "active_filter": filter_type,
    })


@login_required
def mark_all_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return redirect("notifications")


@login_required
def mark_read(request, id):
    notif = get_object_or_404(Notification, id=id, user=request.user)
    notif.is_read = True
    notif.save(update_fields=["is_read"])
    return redirect("notifications")


@login_required
def notifications_delete(request, id):
    notif = get_object_or_404(Notification, id=id, user=request.user)
    notif.delete()
    return redirect("notifications")
