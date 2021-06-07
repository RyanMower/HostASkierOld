from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Host
from .forms import HostForm
from django.contrib import messages
from account.models import Account
from urllib.parse import urlencode
import geopy.distance
import yaml
import requests 



def get_api_key():
    fname = "secrets.yaml"
    try:
        fh = open(fname, "r")
    except:
        print("Could not open file: " + fname)
        exit(1)

    data = yaml.load(fh, Loader=yaml.FullLoader)
    fh.close()

    return data['google_geolocation']['api_key']




def get_lat_long(address):
    data_type = 'json'
    endpoint = f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
    params = {
        "address" : address,
        "key" : get_api_key()
    }
    url_params = urlencode(params)
    url = f'{endpoint}?{url_params}'

    r = requests.get(url)

    if r.status_code not in range(200, 299):
        return {}
    
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng


def check_lat_lon(latlng):
    flag1 = False
    flag2 = False
    if ('lat' in latlng):
        if int(latlng['lat']) != 0:
            flag1 = True
    if ('lng' in latlng):
        if int(latlng['lng']) != 0:
            flag2 = True
    return (flag1 and flag2)


def set_lat_lon(form):
    address = f'{form.address_1} {form.city} {form.state} {form.zip_code} {form.country}'
    latlng = get_lat_long(address)
    if (check_lat_lon(latlng)):
        form.latitude  = latlng['lat']
        form.longitude = latlng['lng']
        return True

    return False
    
    
@login_required
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
