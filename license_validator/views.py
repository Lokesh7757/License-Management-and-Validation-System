# license_validator/views.py
from django.shortcuts import render
from .models import License
from .forms import LicenseForm

def validate_license(request):
    result = None
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            license_number = form.cleaned_data['license_number']
            # Check if the license number exists in the database
            if License.objects.filter(license_number=license_number).exists():
                result = 'Valid'
            else:
                result = 'Invalid'
    else:
        form = LicenseForm()
    
    return render(request, 'license_validator/validate.html', {'form': form, 'result': result})
