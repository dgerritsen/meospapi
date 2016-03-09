from vehicles.models import Vehicle, VehicleSignal
from rest_framework import routers, serializers, viewsets


class VehicleSignalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleSignal
        fields = (
            'id',
            'code',
            'status',
            'start_date',
            'organization',
            'reference',
        )


class VehicleSignalViewSet(viewsets.ModelViewSet):
    queryset = VehicleSignal.objects.all()
    serializer_class = VehicleSignalSerializer


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    signals = VehicleSignalSerializer(many=True)

    class Meta:
        model = Vehicle
        fields = (
            'id',
            'url',
            'license',
            'brand',
            'type',
            'category',
            'vin',
            'apk_valid_until',
            'insured',
            'insurance_company',
            'insurance_valid_until',
            'duplicates',
            'signals',
        )


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer