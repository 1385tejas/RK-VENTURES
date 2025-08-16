from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse
from django.utils.html import format_html

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email', 'get_name', 'get_phone', 'get_budget', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'profile__name', 'profile__phone', 'profile__budget')

    def get_name(self, obj):
        return obj.profile.name if hasattr(obj, 'profile') else ''
    get_name.short_description = 'Name'

    def get_phone(self, obj):
        return obj.profile.phone if hasattr(obj, 'profile') else ''
    get_phone.short_description = 'Phone'

    def get_budget(self, obj):
        return obj.profile.budget if hasattr(obj, 'profile') and obj.profile.budget else ''
    get_budget.short_description = 'Budget'

    def changelist_view(self, request, extra_context=None):
        if not extra_context:
            extra_context = {}
        if request.user.is_superuser:
            url = reverse('download_registrations')
            extra_context['download_registrations_link'] = format_html('<a class="button" href="{}" style="margin:10px 0;">Download User Registrations Excel</a>', url)
        return super().changelist_view(request, extra_context=extra_context)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
