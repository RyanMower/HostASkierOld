from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Host
from .forms import HostForm

@login_required
def become_a_host_view(request):
    form = HostForm(request.POST or None)

    if form.is_valid():
        pre_save = form.save(commit=False)
        pre_save.hostest = request.user
        pre_save.save()
        
    context = {
        'form': form
    }
    return render(request, "becomeahost/becomeahost.html", context)