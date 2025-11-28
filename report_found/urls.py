from django.urls import path
from . import views
urlpatterns = [
    path('report_found/', views.report_found, name='ReportFound'),
]