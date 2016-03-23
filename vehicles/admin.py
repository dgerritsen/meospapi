from django.contrib import admin
from django.utils.safestring import mark_safe
from vehicles.models import Vehicle, VehicleSignal


class VehicleSignalAdmin(admin.StackedInline):
    model = VehicleSignal
    extra = 0


class VehicleAdmin(admin.ModelAdmin):
    inlines = [
        VehicleSignalAdmin,
    ]

    list_display = (
        'license',
        'owner',
        'get_signals',
    )

    def get_signals(self, obj):
        return mark_safe("<br/>".join(["%s voor %s"%(s.code, s.organization) for s in obj.signals.all()]))

admin.site.register(Vehicle, VehicleAdmin)