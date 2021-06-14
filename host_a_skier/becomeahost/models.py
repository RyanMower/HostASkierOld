from django.db import models
from account.models import Account
from users.models import Profile
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext as _



TIMES =      ((0,    '12:00 AM'),
              (0.25, '12:15 AM'),
              (0.5,  '12:30 AM'),
              (0.75, '12:45 AM'),
              (1,    '1:00 AM'),
              (1.25, '1:15 AM'),
              (1.50, '1:30 AM'),
              (1.75, '1:45 AM'),
              (2.00, '2:00 AM'),
              (2.25, '2:15 AM'),
              (2.50, '2:30 AM'),
              (2.75, '2:45 AM'),
              (3.0, '3:00 AM'),
              (3.25, '3:15 AM'),
              (3.5, '3:30 AM'),
              (3.75, '3:45 AM'),
              (4.0, '4:00 AM'),
              (4.25, '4:15 AM'),
              (4.5, '4:30 AM'),
              (4.75, '4:45 AM'),
              (5.0, '5:00 AM'),
              (5.25, '5:15 AM'),
              (5.5, '5:30 AM'),
              (5.75, '5:45 AM'),
              (6.0, '6:00 AM'),
              (6.25, '6:15 AM'),
              (6.5, '6:30 AM'),
              (6.75, '6:45 AM'),
              (7.0, '7:00 AM'),
              (7.25, '7:15 AM'),
              (7.5, '7:30 AM'),
              (7.75, '7:45 AM'),
              (8.0, '8:00 AM'),
              (8.25, '8:15 AM'),
              (8.5, '8:30 AM'),
              (8.75, '8:45 AM'),
              (9.0, '9:00 AM'),
              (9.25, '9:15 AM'),
              (9.5, '9:30 AM'),
              (9.75, '9:45 AM'),
              (10.0, '10:00 AM'),
              (10.25, '10:15 AM'),
              (10.5, '10:30 AM'),
              (10.75, '10:45 AM'),
              (11.0, '11:00 AM'),
              (11.25, '11:15 AM'),
              (11.5, '11:30 AM'),
              (11.75, '11:45 AM'),
              (12.0, '12:00 PM'),
              (12.25, '12:15 PM'),
              (12.5, '12:30 PM'),
              (12.75, '12:45 PM'),
              (13.0, '1:00 PM'),
              (13.25, '1:15 PM'),
              (13.5, '1:30 PM'),
              (13.75, '1:45 PM'),
              (14.0, '2:00 PM'),
              (14.25, '2:15 PM'),
              (14.5, '2:30 PM'),
              (14.75, '2:45 PM'),
              (15.0, '3:00 PM'),
              (15.25, '3:15 PM'),
              (15.5, '3:30 PM'),
              (15.75, '3:45 PM'),
              (16.0, '4:00 PM'),
              (16.25, '4:15 PM'),
              (16.5, '4:30 PM'),
              (16.75, '4:45 PM'),
              (17.0, '5:00 PM'),
              (17.25, '5:15 PM'),
              (17.5, '5:30 PM'),
              (17.75, '5:45 PM'),
              (18.0, '6:00 PM'),
              (18.25, '6:15 PM'),
              (18.5, '6:30 PM'),
              (18.75, '6:45 PM'),
              (19.0, '7:00 PM'),
              (19.25, '7:15 PM'),
              (19.5, '7:30 PM'),
              (19.75, '7:45 PM'),
              (20.0, '8:00 PM'),
              (20.25, '8:15 PM'),
              (20.5, '8:30 PM'),
              (20.75, '8:45 PM'),
              (21.0, '9:00 PM'),
              (21.25, '9:15 PM'),
              (21.5, '9:30 PM'),
              (21.75, '9:45 PM'),
              (22.0, '10:00 PM'),
              (22.25, '10:15 PM'),
              (22.5, '10:30 PM'),
              (22.75, '10:45 PM'),
              (23.0, '11:00 PM'),
              (23.25, '11:15 PM'),
              (23.5, '11:30 PM'),
              (23.75, '11:45 PM'))
              
BOAT_TYPES = ((1, 'Malibu'),
              (2, 'ATX'),
              (3, 'Centurion'),
              (4, 'Nautique'),
              (5, 'MasterCraft'),
              (6, 'Moomba'),
              (7, 'Tige'),
              (8, 'Supra'),
              (9, 'Axis'),
              (10, 'Other'))

WATERSKI_EVENTS =   ((1, 'Slalom'),
                    (2, 'Jump'),
                    (3, 'Trick'),
                    (3, 'Wake Surfing'),
                    (3, 'Wake Boarding'),
                    (4, 'Other'))

def update_optional_user_fields(self):
    if self.address_1 == '':
        self.address_1 = self.hostest.address_1

    if self.address_2 == '':
        self.address_2 = self.hostest.address_2

    if self.city == '':
        self.city = self.hostest.city

    if self.zip_code == '':
        self.zip_code = self.hostest.zip_code

    if self.state == '':
        self.state = self.hostest.state

    if self.country == '':
        self.country = self.hostest.country

    if self.email == '':
        self.email = self.hostest.email

    if self.phone_number == '':
        self.phone_number = self.hostest.phone_number


# Create your models here.
class Host(models.Model):
    address_1 = models.CharField(_("Address 1"), max_length=100, default="123 Street Road", blank=True)
    address_2 = models.CharField(_("Address 2"), max_length=100, blank=True)
    city = models.CharField(_("City"), max_length=100, default="Zanesville", blank=True)
    state = models.CharField(_("State"), max_length=100, default="Minnesota", blank=True)
    zip_code = models.CharField(_("Zip Code"), max_length=5, default="43701", blank=True)
    country = models.CharField(_("Country"), max_length=100, default="USA", blank=True)

    latitude = models.DecimalField(
      max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(
       max_digits=9, decimal_places=6, blank=True, default='0')

    price = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True) #opt
    phone_number = models.CharField(max_length=100, blank=True) #opt

    boat_type = MultiSelectField(choices=BOAT_TYPES) 
    events_can_pull = MultiSelectField(choices=WATERSKI_EVENTS)

    monday    = MultiSelectField(blank=True, choices=TIMES)
    tuesday   = MultiSelectField(blank=True, choices=TIMES)
    wednesday = MultiSelectField(blank=True, choices=TIMES)
    thursday  = MultiSelectField(blank=True, choices=TIMES)
    friday    = MultiSelectField(blank=True, choices=TIMES)
    saturday  = MultiSelectField(blank=True, choices=TIMES)
    sunday    = MultiSelectField(blank=True, choices=TIMES)

    
    
    extra_info = models.TextField(blank=True)

    hostest = models.ForeignKey(Account, on_delete=models.CASCADE)
    

    def save(self, **kwargs):
        update_optional_user_fields(self)
        super().save(**kwargs)
