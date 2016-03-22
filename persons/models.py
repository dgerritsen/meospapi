from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from rest_framework.authtoken.models import Token


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
    dangers = models.ManyToManyField(DangerClass, blank=True)

    def __unicode__(self):
        return self.initials + ' ' + self.last_name + ' (' + self.first_name + ')'

    def display_name(self):
        return self.last_name + ', ' + self.initials + ' (' + self.first_name + ')'

    def keno(self):
        return self.last_name[:4].lower() + self.first_name[0].lower() + self.birth_date.strftime('%y%m%d')

    def danger_list(self):
        return mark_safe("<br/>".join([d.description for d in self.dangers.all()]))


class PersonSignal(models.Model):
    person = models.ForeignKey(Person, related_name='signals')
    code = models.CharField(max_length=10)
    status = models.CharField(max_length=100)
    start_date = models.DateField()
    organization = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    register = models.CharField(max_length=50)

    def __unicode__(self):
        return self.person.display_name() + ' (' + self.register + ')'


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
    form = models.URLField(blank=True, null=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)