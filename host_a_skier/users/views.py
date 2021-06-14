from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm
from account.forms import AccountUpdateForm
from django.contrib.auth.decorators import login_required

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
