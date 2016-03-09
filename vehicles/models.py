from __future__ import unicode_literals
from django.db import models
from persons.models import Person


class Vehicle(models.Model):
    owner = models.ForeignKey(Person)
    license = models.CharField(max_length=20)
    vin = models.CharField(max_length=40)
    apk_valid_until = models.DateField()
    brand = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    category = models.CharField(max_length=40)

    insured = models.BooleanField(default=True)
    insurance_company = models.CharField(max_length=40)
    insurance_valid_until = models.DateField()

    duplicates = models.IntegerField(default=0)

    def __unicode__(self):
        return self.license


class VehicleSignal(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='signals')
    code = models.CharField(max_length=10)
    status = models.CharField(max_length=100)
    start_date = models.DateField()
    organization = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)

    def __unicode__(self):
        return self.vehicle + ' (' + self.code + ')'