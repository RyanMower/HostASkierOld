from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Host
from .forms import HostForm
from django.contrib import messages
from account.models import Account
import geopy.distance

def check_lat_lon(form):
    if int(form.latitude) == 0:
        return False
    if int(form.longitude) == 0:
        return False
    return True

@login_required
def become_a_host_view(request):
    form = HostForm(request.POST or None)
    
    if form.is_valid():
        pre_save = form.save(commit=False)
        pre_save.hostest = request.user
        if (check_lat_lon(pre_save)):
            pre_save.save()
            messages.success(request, f'{request.user.username}\'s Ski spot created successfully')
            return redirect('hostaskier-home')
        else:
            messages.error(request, f'{request.user.username}\'s Please enter a valid address.')
        
        
    context = {
        'form': form
    }
    return render(request, "becomeahost/becomeahost.html", context)
