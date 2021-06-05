from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Host
from .forms import HostForm
from django.contrib import messages
from account.models import Account


@login_required
def become_a_host_view(request):
    form = HostForm(request.POST or None)
    
    if form.is_valid():
        pre_save = form.save(commit=False)
        pre_save.hostest = request.user
        pre_save.save()
        messages.success(request, f'{request.user.username}\'s Ski spot created successfully')
        return redirect('hostaskier-home')
        
    context = {
        'form': form
    }
    return render(request, "becomeahost/becomeahost.html", context)
