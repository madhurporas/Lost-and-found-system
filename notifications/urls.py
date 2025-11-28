from django.urls import path
from . import views

urlpatterns = [
    path("notifications/", views.notifications_page, name="notifications"),
    path("notifications/mark-all-read/", views.mark_all_read, name="notifications_mark_all_read"),
    path("notifications/mark-read/<int:id>/", views.mark_read, name="notifications_mark_read"),
    path("notifications/delete/<int:id>/", views.notifications_delete, name="notifications_delete"),
]
