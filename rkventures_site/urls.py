"""
URL configuration for rkventures_site project.

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
from properties import views as property_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', property_views.home, name='home'),
    path('about/', property_views.about, name='about'),
    path('contact/', property_views.contact, name='contact'),
    path('properties/', property_views.properties_list, name='properties_list'),
    path('properties/<int:property_id>/', property_views.property_detail, name='property_detail'),
    path('properties/<int:property_id>/edit/', property_views.property_edit, name='property_edit'),
    path('properties/<int:property_id>/delete/', property_views.property_delete, name='property_delete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('upload-properties/', property_views.upload_properties, name='upload_properties'),
    path('notifications/', include('notifications.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
