from django.urls import path
from . import views
urlpatterns = [
    path('view_user/', views.view_profile_info, name='ProfileInfo'),
]