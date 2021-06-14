from django import forms
from account.models import Account
from django.contrib.auth.forms import UserCreationForm

# new class adds email field to usercreation form
class AccountRegisterForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['username', 
                  'email', 
                  'address_1', 
                  'address_2', 
                  'city', 
                  'state', 
                  'zip_code', 
                  'country', 
                  'phone_number', 
                  'password1', 
                  'password2'
                  ]

class AccountUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username',
                  'email',
                  'address_1',
                  'address_2',
                  'city',
                  'state',
                  'zip_code',
                  'country', 
                  'phone_number',
                  ]

