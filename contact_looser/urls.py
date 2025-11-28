from django.urls import path
from . import views
urlpatterns = [
    path('contact_looser/<int:id>/', views.cont_looser, name='ContactLooser'),
   

]