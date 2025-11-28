from django.urls import path
from . import views
urlpatterns = [
    path('report_lost/', views.report_lost, name='ReportLost')
]