""""Forms to User"""

# Django
from django import forms

class FormPpdateProfile(forms.Form):
    """Form to update profile"""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=True)