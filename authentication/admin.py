from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('username',)
    search_fields=['username']

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

admin.site.register(Profile, ProfileAdmin)