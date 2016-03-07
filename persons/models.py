from __future__ import unicode_literals

from django.db import models


DANGER_CLASSES = (
    (1, 'Vuurwapengevaarlijk'),
    (2, 'Verzetpleger'),
    (3, 'Harddrugs gebruiker'),
    (4, 'Alcoholist'),
    (5, 'Vluchtgevaarlijk'),
    (6, 'Medische indicatie'),
    (7, 'Zelfmoord neigingen'),
    (8, 'Psychiatrisch patient'),
)


class DangerClass(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description

GENDERS = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('u', 'Unknown'),
)


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    initials = models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=GENDERS)
    bsn = models.CharField(max_length=30)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200)
    birth_country = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    dangers = models.ManyToManyField(DangerClass)

    def __unicode__(self):
        return self.initials + ' ' + self.last_name + ' (' + self.first_name + ')'

    def display_name(self):
        return self.last_name + ', ' + self.initials + ' (' + self.first_name + ')'

    def keno(self):
        return self.last_name[:3] + self.first_name[0] + self.birth_date.strftime('%y%m%d')


class DriversLicense(models.Model):
    person = models.ForeignKey(Person, related_name='driverslicenses')
    number = models.CharField(max_length=30)
    country = models.CharField(max_length=200)
    date = models.DateField()
    authority = models.CharField(max_length=200)
    category = models.CharField(max_length=5)
    valid_until = models.DateField()
    address = models.CharField(max_length=200)


class Address(models.Model):
    person = models.ForeignKey(Person, related_name='addresses')
    town = models.CharField(max_length=50) # Gemeente
    city = models.CharField(max_length=100) # Stad
    postal_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    country = models.CharField(max_length=50)


class Registration(models.Model):
    person = models.ForeignKey(Person, related_name='registrations')
    title = models.CharField(max_length=200)
    mk = models.CharField(max_length=200)
    role = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    date = models.DateField(blank=True, null=True)

