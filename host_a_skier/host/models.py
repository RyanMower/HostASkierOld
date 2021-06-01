from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Host(models.Model):
    # If blank, use the address of the currently logged in user
    street_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100) # make this a choices drop down?
    # lat 
    # long

    price = models.CharField(max_length=100)
    email = models.CharField(max_length=100) #opt
    phone_number = models.CharField(max_length=100) #opt

    boat_type = models.CharField(max_length=100) # MAKE THIS A CHOICES DROP DOWN
    events_can_pull = models.CharField(max_length=100) # Make this a multiple choices drop down!

    hostest = models.ForeignKey(User, on_delete=models.CASCADE)

    extra_info = content = models.TextField()

