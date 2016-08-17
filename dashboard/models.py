from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.gis.db import models as gismodels
from phonenumber_field.modelfields import PhoneNumberField

class PriceList(models.Model):
    EXCHANGES_PER_WEEK = (
        (0.25, 0.25),
        (0.5, 0.5),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7)
    )
    mat_length = models.IntegerField(default=150, verbose_name="Length")
    mat_width = models.IntegerField(default=85, verbose_name="Width")
    exchanges_per_week = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        choices=EXCHANGES_PER_WEEK,
        verbose_name="Exchanges per week")
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(verbose_name="Price added", editable=False)
    updated = models.DateTimeField(verbose_name="Price updated")

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(PriceList, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.price_per_day) or u''

    class Meta:
            verbose_name_plural = "priceList"


class Clients(models.Model):
    client_name = models.CharField(max_length=100, verbose_name="Name")
    aggreement_nbr = models.CharField(max_length=30, verbose_name="Aggreement NBR", blank=True)
    edrpou_code = models.CharField(max_length=12, verbose_name="EDRPOU Code", blank=True)
    mfo_code = models.CharField(max_length=6, verbose_name="MFO", blank=True)
    account_nbr = models.CharField(max_length=12, verbose_name="Account NBR", blank=True)
    client_addresses_quantity = models.IntegerField(verbose_name="Addresses quantity")
    resp_person_first_name = models.CharField(max_length=30, verbose_name="Responsible person first name", blank=True)
    resp_person_last_name = models.CharField(max_length=30, verbose_name="Responsible person last name", blank=True)
    resp_person_middle_name = models.CharField(max_length=30, verbose_name="Responsible person middle name", blank=True)
    passport_nbr = models.CharField(max_length=30, verbose_name="Passport NBR", blank=True)
    identification_code = models.CharField(max_length=12, verbose_name="Identification code", blank=True)
    registration_address = models.CharField(max_length=200, verbose_name="Registration Address", blank=True)
    post_address = models.CharField(max_length=200, verbose_name="Post Address", blank=True)
    bank_name = models.CharField(max_length=50, verbose_name="Bank name", blank=True)
    client_email = models.EmailField(verbose_name="Client e-mail address", blank=True)
    client_phone_nbr = PhoneNumberField(blank=True)
    client_details = models.TextField(verbose_name="Client details", blank=True)
    client_discount_rate = models.IntegerField(verbose_name="Discount rate", default=0)
    client_price_per_day = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    created = models.DateTimeField(verbose_name="Client added", editable=False)
    updated = models.DateTimeField(verbose_name="Client updated")

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Clients, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.client_name

    def get_fields(self):
        return [(field.verbose_name, field._get_val_from_obj(self)) for field in Clients._meta.fields]

    class Meta:
            verbose_name_plural = "clients"


class ClientsAddresses(gismodels.Model):
    EXCHANGES_PER_WEEK = (
        (0.25, 0.25),
        (0.5, 0.5),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7)
    )
    location_name = models.CharField(max_length=50, verbose_name="Location name")
    address_city = models.CharField(max_length=50, verbose_name="City", blank=True)
    address_street = models.CharField(max_length=100, verbose_name="Street", blank=True)
    address_building = models.CharField(max_length=10, verbose_name="Building", blank=True)
    address_details = models.TextField(verbose_name="Address details", blank=True)
    geo_point = gismodels.PointField(verbose_name="Point")
    created = models.DateTimeField(verbose_name="Address added", editable=False)
    updated = models.DateTimeField(verbose_name="Address updated")
    exchanges_per_week = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        choices=EXCHANGES_PER_WEEK,
        verbose_name="Exchanges per week")

    client = models.ForeignKey(Clients, models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(ClientsAddresses, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.location_name

    def get_fields(self):
        return [(field.verbose_name, field._get_val_from_obj(self)) for field in ClientsAddresses._meta.fields]

    class Meta:
            verbose_name_plural = "clientAddresses"


class Mats(models.Model):
    mat_length = models.IntegerField(default=150, verbose_name="Length")
    mat_width = models.IntegerField(default=85, verbose_name="Width")
    mat_color = models.CharField(max_length=50, default="Granite", verbose_name="Color")
    created = models.DateTimeField(verbose_name="Mat added", editable=False)
    updated = models.DateTimeField(verbose_name="Mat updated")

    clients_addresses = models.ForeignKey(ClientsAddresses, models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Mats, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.mat_color

    def get_fields(self):
        return [(field.verbose_name, field._get_val_from_obj(self)) for field in Mats._meta.fields]

    class Meta:
            verbose_name_plural = "mats"

# Create your models here.
