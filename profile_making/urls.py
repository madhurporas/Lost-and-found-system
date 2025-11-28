from django.urls import path
from . import views
urlpatterns = [
    path('create_profile/', views.make_profile, name='Make_Profile')
]