from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Notification
from django.views.decorators.http import require_POST

# Create your views here.

@login_required
def user_notifications_api(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')[:20]
    data = [
        {
            'id': n.id,
            'title': n.title,
            'message': n.message,
            'created_at': n.created_at.strftime('%Y-%m-%d %H:%M'),
            'read': n.read,
            'property_id': n.property.id if n.property else None,
        }
        for n in notifications
    ]
    return JsonResponse({'notifications': data})

@require_POST
@login_required
def mark_notification_read(request):
    notif_id = request.POST.get('id')
    try:
        notif = Notification.objects.get(id=notif_id, user=request.user)
        notif.read = True
        notif.save()
        return JsonResponse({'success': True})
    except Notification.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Notification not found.'}, status=404)

@require_POST
@login_required
def delete_notification(request):
    notif_id = request.POST.get('id')
    try:
        notif = Notification.objects.get(id=notif_id, user=request.user)
        notif.delete()
        return JsonResponse({'success': True})
    except Notification.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Notification not found.'}, status=404)

@require_POST
@login_required
def clear_all_notifications(request):
    Notification.objects.filter(user=request.user).delete()
    return JsonResponse({'success': True})
