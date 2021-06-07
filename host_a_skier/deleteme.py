
def set_lat_lon(form):
    #url = f'{request.user.address_1} {request.user.city}'
    #print(f"-------->{form.address_1} {from.city}")
    return True
    
    
#@login_required
def become_a_host_view(request):
    form = HostForm(request.POST or None)
    
    if form.is_valid():
        pre_save = form.save(commit=False)
        pre_save.hostest = request.user
        if (set_lat_lon(pre_save)):
            pre_save.save()
            messages.success(request, f'{request.user.username}\'s Ski spot created successfully')
            return redirect('hostaskier-home')
        else:
            messages.error(request, f'{request.user.username}\'s Please enter a valid address.')
        
        
    context = {
        'form': form
    }
    return render(request, "becomeahost/becomeahost.html", context)

