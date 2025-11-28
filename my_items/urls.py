from django.urls import path
from . import views
urlpatterns = [
    path('my_items/', views.my_items, name='MyItems')
]