from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import AccountRegisterForm
from .forms import AccountUpdateForm
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):

    # determines whether the form is being submitted or visited
    # is a POST request when being submitted
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)

        # check validity of form
        if form.is_valid():

            # saves user
            form.save()

            #displays success message and redirects to homepage
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}\'s account created successfully')
            return redirect('login')

    else:
        form = AccountRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):

    # create an instance of a user update form
    # and a profile update form
    if request.method == 'POST':
        u_form = AccountUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'changes updated successfully')
            return redirect('profile')
    else:
        
        u_form = AccountUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    # pass both forms into render as a context dictionary
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
