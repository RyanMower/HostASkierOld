from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django import forms
from django_countries.fields import CountryField

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, address_1, address_2, 
                    city, zip_code, state, country, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email.")
        if not username:
            raise ValueError("Users must have a username.")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            address_1 = address_1,
            address_2 = address_2,
            city = city,
            zip_code = zip_code,
            state = state,
            country = country,
            phone_number = phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username     = username,
            password     = password,
            address_1    = 'admin',
            address_2    = 'admin', 
            city         = 'admin',
            zip_code     = 'admin',
            state        = 'admin',
            country      = 'admin',
            phone_number = 'admin',
        )

        user.is_admin     = True
        user.is_staff     = True
        user.is_active    = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email        = models.EmailField(unique=True)
    username     = models.CharField(max_length=30, unique=True)
    date_joined  = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login   = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    ## My Fields ##
    address_1 = models.CharField(_("Address 1"), max_length=100, default="123 Street Road")
    address_2 = models.CharField(_("Address 2"), max_length=100, blank=True)
    city = models.CharField(_("City"), max_length=100, default="Zanesville")
    zip_code = models.CharField(_("Zip Code"), max_length=5, default="43701")
    state = models.CharField(_("State"), max_length=100, default="Minnesota")
    country = models.CharField(_("State"), max_length=100, default="Minnesota")


    latitude = models.DecimalField(
      max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(
       max_digits=9, decimal_places=6, blank=True, default='0')
        
    phone_number = models.CharField(max_length=100)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username',
                    #    'address_1', 
                    #    'address_2',
                    #    'city',
                    #    'zip_code',
                    #    'state',
                    #    'country',
                    #    'phone_number',
                       ]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_laber):
        return True
