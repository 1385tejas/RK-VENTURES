from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def health_check(request):
    """Simple health check endpoint for debugging"""
    return JsonResponse({
        'status': 'healthy',
        'message': 'RK Ventures is running successfully!'
    })
