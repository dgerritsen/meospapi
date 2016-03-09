from django.contrib import admin
from vehicles.models import Vehicle, VehicleSignal


class VehicleSignalAdmin(admin.StackedInline):
    model = VehicleSignal
    extra = 0


class VehicleAdmin(admin.ModelAdmin):
    inlines = [
        VehicleSignalAdmin,
    ]

admin.site.register(Vehicle, VehicleAdmin)