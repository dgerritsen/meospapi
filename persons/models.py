from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    initials = models.CharField(max_length=50)
    bsn = models.CharField(max_length=30)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200)

    def __unicode__(self):
        return self.initials + ' ' + self.last_name + ' (' + self.first_name + ')'

    def display_name(self):
        return self.last_name + ', ' + self.initials + ' (' + self.first_name + ')'


class DriversLicense(models.Model):
    person = models.ForeignKey(Person, related_name='driverslicenses')
    number = models.CharField(max_length=30)
    country = models.CharField(max_length=200)
    date = models.DateField()
    authority = models.CharField(max_length=200)
    category = models.CharField(max_length=5)
    valid_until = models.DateField()
    address = models.CharField(max_length=200)

