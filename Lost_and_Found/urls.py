"""
URL configuration for Lost_and_Found project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_finder/', include("contact_finder.urls")),
    path('contact_looser/', include("contact_looser.urls")),
    path('home/', include("home.urls")),
    path('', include("Landing_page.urls")),
    path('my_items/', include("my_items.urls")),
    path('notifications/', include("notifications.urls")),
    path('profile_making/', include("profile_making.urls")),
    path('report_found/', include("report_found.urls")),
    path('report_lost/', include("report_lost.urls")),
    path('users/', include("users.urls")),
    path('view_profile/', include("view_profile.urls")),
    path('messages/', include("inappmessages.urls")),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
