from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.user_notifications_api, name='user_notifications_api'),
    path('api/mark_read/', views.mark_notification_read, name='mark_notification_read'),
    path('api/delete/', views.delete_notification, name='delete_notification'),
    path('api/clear_all/', views.clear_all_notifications, name='clear_all_notifications'),
] 