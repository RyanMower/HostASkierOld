from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import AccountRegisterForm
from .forms import AccountUpdateForm

def check_lat_lon(form):
    if int(form.latitude) == 0:
        return False
    if int(form.longitude) == 0:
        return False
    return True

def register(request):

    # determines whether the form is being submitted or visited
    # is a POST request when being submitted
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)

        # check validity of form
        if form.is_valid():

            # saves user
            pre_save = form.save(commit=False)
            if (check_lat_lon(pre_save)):
                #displays success message and redirects to homepage
                pre_save.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'{username}\'s account created successfully')
                return redirect('login')
            else:
                messages.error(request, 'Please enter a valid address.')

    else:
        form = AccountRegisterForm()
    return render(request, 'users/register.html', {'form':form})
