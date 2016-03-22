from django.contrib import admin
from django.utils.safestring import mark_safe
from persons.models import Person, PersonSignal, DriversLicense, Address, Registration, DangerClass


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

    list_display = (
        'display_name',
        'keno',
        'gender',
        'get_licenses',
        'get_registrations',
        'danger_list',
        'get_signals',
    )

    def get_signals(self, obj):
        return mark_safe("<br/>".join(["%s voor %s"%(s.code, s.organization) for s in obj.signals.all()]))
    get_signals.short_description = 'Signals'

    def get_registrations(self, obj):
        return mark_safe("<br/>".join(["%s (%s)"%(s.mk, s.role) for s in obj.registrations.all()]))
    get_registrations.short_description = 'Registrations'

    def get_licenses(self, obj):
        return ", ".join(["%s"%(s.category) for s in obj.driverslicenses.all()])
    get_licenses.short_description = 'Drivers Licenses'

admin.site.register(Person, PersonAdmin)
admin.site.register(DangerClass)