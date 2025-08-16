from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20, choices=[('broker', 'Broker'), ('buyer', 'Buyer'), ('investor', 'Investor')], default='buyer')
    interested_places = models.TextField(blank=True, null=True)
    budget = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. 50L-1Cr, 1Cr-2Cr, etc.")

    def __str__(self):
        return self.user.username
