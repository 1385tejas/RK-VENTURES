from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
import openpyxl
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        user_type = request.POST.get('user_type', 'buyer')
        interested_places = request.POST.get('interested_places', '')
        budget = request.POST.get('budget', '')
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'accounts/register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'accounts/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'accounts/register.html')
        user = User.objects.create_user(username=username, password=password, email=email)
        profile = user.profile  # Created by signal
        profile.name = name
        profile.phone = phone
        profile.user_type = user_type
        profile.interested_places = interested_places
        profile.budget = budget
        profile.save()
        # Save registration to Excel
        excel_path = os.path.join(settings.MEDIA_ROOT, 'registrations.xlsx')
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        if os.path.exists(excel_path):
            wb = openpyxl.load_workbook(excel_path)
            ws = wb.active
        else:
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.append(['Username', 'Name', 'Phone', 'Email', 'User Type', 'Interested Places', 'Budget'])
        ws.append([username, name, phone, email, user_type, interested_places, budget])
        wb.save(excel_path)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        identifier = request.POST['identifier']
        password = request.POST['password']
        user = None
        # Try username
        user = authenticate(request, username=identifier, password=password)
        if not user:
            # Try email
            try:
                user_obj = User.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        if not user:
            # Try phone (via Profile)
            try:
                profile = Profile.objects.get(phone=identifier)
                user = authenticate(request, username=profile.user.username, password=password)
            except Profile.DoesNotExist:
                pass
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@user_passes_test(lambda u: u.is_superuser)
def download_registrations_excel(request):
    excel_path = os.path.join(settings.MEDIA_ROOT, 'registrations.xlsx')
    if not os.path.exists(excel_path):
        return HttpResponse('No registrations file found.', content_type='text/plain')
    with open(excel_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=registrations.xlsx'
        return response
