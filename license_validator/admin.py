# license_validator/admin.py
from django.contrib import admin
from .models import License

admin.site.register(License)
