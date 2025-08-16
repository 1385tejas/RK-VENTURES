from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    main_image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    extra_images = models.JSONField(default=list, blank=True)  # List of image URLs
    extra_data = models.JSONField(default=dict, blank=True)    # For any extra fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"Property #{self.id}"
