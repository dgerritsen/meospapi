from persons.models import Person, DriversLicense
from rest_framework import routers, serializers, viewsets


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    driverslicenses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ('url', 'display_name', 'initials', 'first_name', 'last_name', 'bsn', 'birth_date', 'birth_place', 'driverslicenses')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DriverslicenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DriversLicense
        fields = ('url', 'person', 'number', 'country', 'category', 'authority', 'date', 'valid_until', 'address')


class DriverslicenseViewSet(viewsets.ModelViewSet):
    queryset = DriversLicense.objects.all()
    serializer_class = DriverslicenseSerializer