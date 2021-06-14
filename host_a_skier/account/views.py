from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import AccountRegisterForm
from .forms import AccountUpdateForm
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
    


def register(request):

    # determines whether the form is being submitted or visited
    # is a POST request when being submitted
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)

        # check validity of form
        if form.is_valid():

            # saves user
            pre_save = form.save(commit=False)
            if (set_lat_lon(pre_save)):
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
