from django.contrib import admin
from persons.models import Person, PersonSignal, DriversLicense, Address, Registration


class DriversLicenseAdmin(admin.StackedInline):
    model = DriversLicense
    extra = 0


class AddressAdmin(admin.StackedInline):
    model = Address
    extra = 0


class RegistrationAdmin(admin.StackedInline):
    model = Registration
    extra = 0


class PersonSignalAdmin(admin.StackedInline):
    model = PersonSignal
    extra = 0


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        DriversLicenseAdmin,
        AddressAdmin,
        RegistrationAdmin,
        PersonSignalAdmin,
    ]

admin.site.register(Person, PersonAdmin)