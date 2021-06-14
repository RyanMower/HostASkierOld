from django import forms
from .models import Host

class HostForm(forms.ModelForm):
    
    class Meta:
        model = Host
        fields = [
            'address_1',
            'address_2', 
            'city',
            'state',
            'zip_code',
            'country',
            'price',
            'email',
            'phone_number',
            'boat_type',
            'events_can_pull',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            'extra_info'
        ]