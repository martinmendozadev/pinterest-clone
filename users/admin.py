"""User admin classes."""

# Django
from django.contrib import admin

# Models
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    pass