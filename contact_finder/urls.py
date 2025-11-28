from django.urls import path
from . import views
urlpatterns = [
    path('contact_finder/<int:id>/',views.cont_finder, name='ContactFinder')
]