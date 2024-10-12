# license_validator/forms.py
from django import forms

class LicenseForm(forms.Form):
    license_number = forms.CharField(max_length=100, label='License Number')
