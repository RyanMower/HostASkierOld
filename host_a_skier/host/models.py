from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django_countries.fields import CountryField
import requests

# Create your models here.
class Host(models.Model):
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    # If blank, use the address of the currently logged in user
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=100)
    country = CountryField(blank=True)

    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')

    price = models.CharField(max_length=100)
    email = models.CharField(max_length=100) #opt
    phone_number = models.CharField(max_length=100) #opt

    boat_type = models.CharField(max_length=100) # MAKE THIS A CHOICES DROP DOWN
    events_can_pull = models.CharField(max_length=100) # Make this a multiple choices drop down!

    hostest = models.ForeignKey(User, on_delete=models.CASCADE)

    extra_info = content = models.TextField()

    def save(self, **kwargs):
        super().save(**kwargs)

        # address = " ".join(
        #     [self.address_1, self.address_2, str(self.zip_code), self.city])
        # api_key = "PROJECT_API_KEY"
        # api_response = requests.get(
        #     'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        # api_response_dict = api_response.json()

        # if api_response_dict['status'] == 'OK':
        #     self.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        #     self.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        #     super().save(**kwargs)


