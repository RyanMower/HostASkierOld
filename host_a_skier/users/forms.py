from django import forms
from account.models import Account
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# new class adds email field to usercreation form
class AccountRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']

class AccountUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

