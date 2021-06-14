from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm
from account.forms import AccountUpdateForm
from becomeahost.forms import HostUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):

    # create an instance of a user update form
    # and a profile update form
    if request.method == 'POST':
        a_form = AccountUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if a_form.is_valid() and p_form.is_valid():
            a_form.save()
            p_form.save()
            messages.success(request, 'changes updated successfully')
            return redirect('profile')
    else:
        
        a_form = AccountUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'a_form': a_form,
            'p_form': p_form,
        }

    return render(request, 'users/profile.html', context)
