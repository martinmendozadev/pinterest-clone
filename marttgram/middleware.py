"""Middleware for user profile"""

# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfleCompleteMiddleware:

    def __init__(self, get_response):
        """Middlewere initialization"""
        self.get_response = get_response
        

    def __call__(self, request):
        """
            All users need have profile photo and biography
        """

        if not request.user.is_anonymous:
            if not request.user.is_staff:
                user = request.user.profile
                if not user.picture or not user.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')        

        response = self.get_response(request)
        return response