# license_validator/models.py
from django.db import models

class License(models.Model):
    license_number = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.license_number
