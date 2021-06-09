from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FindMyHostForm, FindMyHostForm_DifferentAddress
from django.contrib import messages
from account.models import Account
from urllib.parse import urlencode
from  geopy import distance
import yaml
import requests 
from becomeahost.models import Host
from math import radians, cos, sin, asin, sqrt


## ------------------------------- ##
## ------ HELPER FUNCTIONS  ------ ##
## ------------------------------- ##

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

def modified_addr(form):
    modified_addr = False
    if form.cleaned_data.get("address_1") != '':
        modified_addr = True
    if form.cleaned_data.get("address_2") != '':
        modified_addr = True
    if form.cleaned_data.get("city") != '':
        modified_addr = True 
    if form.cleaned_data.get("state") != '':
        modified_addr = True
    if form.cleaned_data.get("country") != '':
        modified_addr = True
    return modified_addr

# returns true if inside radius, otherwise false
def is_within_radius(coords_1, coords_2, radius):

    # convert to radians
    lat_1, lon_1, lat_2, lon_2 = map(radians, [coords_1[0], coords_1[1], coords_2[0], coords_2[1]])

    # haversine
    dlon = lon_2 - lon_1
    dlat = lat_2 - lat_1
    a = sin(dlat/2)**2 + cos(lat_1) * cos(lat_2) * sin(dlon/2)**2
    c = 2 * sin(sqrt(a))
    x = c * 3956 # 6371 for kilometers
    return x <= radius

## ------------------------------- ##
## ------ FILTER FUNCTIONS  ------ ##
## ------------------------------- ##
def get_hosts():
    return Host.objects.all()

def filter_on_distance(hosts, form, search_form, latlng, request):
    new_hosts = []
    print(search_form.cleaned_data.get("willing_distance"))
    if search_form.cleaned_data.get("willing_distance") == '5':
        print("in here")
        return hosts

    if not check_lat_lon(latlng):
        latlng['lat'] = request.user.latitude
        latlng['lng'] = request.user.longitude

    distance = float(search_form.cleaned_data.get("willing_distance"))

    coords_1 = (latlng['lat'], latlng['lng'])

    for host in hosts:
        coords_2 = (host.latitude, host.longitude)
        #ans = (distance.distance(coords_1, coords_2).miles)
        #ans = distance.great_circle(coords_1, coords_2).miles
        if is_within_radius(coords_1, coords_2, distance):
            new_hosts.append(host)

    return new_hosts

def filter_on_email(hosts, form):
    new_hosts = []
    if form.cleaned_data.get("email") != '':
        for host in hosts:
            if host.email == form.cleaned_data.get("email"):
                new_hosts.append(host)
    else:
        print("in here")
        new_hosts = hosts
    return new_hosts

def filter_on_phonenumber(hosts, form):
    new_hosts = []
    if form.cleaned_data.get("phone_number") != '':
        for host in hosts:
            if host.phone_number == form.cleaned_data.get("phone_number"):
                new_hosts.append(host)
    else:
        print("in here")
        new_hosts = hosts
    return new_hosts

def filter_on_price(hosts, form):
    return hosts

def filter_on_time(hosts, form):
    return hosts

def filter_on_boattype(hosts, form):
    return hosts

def filter_on_event(hosts, form):
    return hosts

def filter_hosts(search_form, address_form, latlng, request):
    hosts = get_hosts()
    hosts = filter_on_distance(hosts, address_form, search_form, latlng, request)
    hosts = filter_on_email(hosts, search_form)
    hosts = filter_on_phonenumber(hosts, search_form)
    hosts = filter_on_price(hosts, search_form)
    hosts = filter_on_time(hosts, search_form)
    hosts = filter_on_boattype(hosts, search_form)
    hosts = filter_on_event(hosts, search_form)
    return hosts

@login_required
def findmyhost_view(request):
    search_form = FindMyHostForm(request.POST or None)
    address_form = FindMyHostForm_DifferentAddress(request.POST or None)

    context = {
        'search_form' : search_form,
        'address_form': address_form,
    }

    if request.method == 'POST':
        if search_form.is_valid() and address_form.is_valid():
            latlng = {}
            if (modified_addr(address_form)):
                new_addr = f'{address_form.address_1} {address_form.city} {address_form.state} {address_form.zip_code} {address_form.country}'
                latlng = get_lat_long(new_addr)

                if (check_lat_lon(latlng)):
                    context['hosts'] = filter_hosts(search_form, address_form, latlng, request)
                    print(context)
                else:
                    messages.error(request, f'{request.user.username}\'s Please enter a valid address.')
            else:
                 context['hosts'] = filter_hosts(search_form, address_form, latlng, request)
        else:
            messages.error(request, f'{request.user.username}\'s The provided form was not valid.')
    else: 
        context['hosts'] = get_hosts()  ## First time accessing page, return all Hosts
        
    return render(request, "findmyhost/findmyhost.html", context)
