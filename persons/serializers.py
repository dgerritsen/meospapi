from persons.models import Person, PersonSignal, DriversLicense, DangerClass, Registration, Address
from rest_framework import routers, serializers, viewsets


class DangerClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DangerClass
        fields = ('id', 'url', 'code', 'description')


class DangerClassViewSet(viewsets.ModelViewSet):
    queryset = DangerClass.objects.all()
    serializer_class = DangerClassSerializer


class DriverslicenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DriversLicense
        fields = ('url', 'person', 'number', 'country', 'category', 'authority', 'date', 'valid_until', 'address')


class DriverslicenseViewSet(viewsets.ModelViewSet):
    queryset = DriversLicense.objects.all()
    serializer_class = DriverslicenseSerializer


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'url', 'person', 'town', 'city', 'postal_code', 'street', 'number', 'country')


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = ('id', 'url', 'person', 'title', 'mk', 'role', 'type', 'date')


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class PersonSignalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonSignal
        fields = (
            'id',
            'url',
            'code',
            'status',
            'start_date',
            'organization',
            'reference',
            'register',
        )


class PersonSignalViewSet(viewsets.ModelViewSet):
    queryset = PersonSignal.objects.all()
    serializer_class = PersonSignalSerializer


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    driverslicenses = DriverslicenseSerializer(many=True)
    dangers = DangerClassSerializer(many=True)
    registrations = RegistrationSerializer(many=True)
    addresses = AddressSerializer(many=True)
    signals = PersonSignalSerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'url',
            'keno',
            'display_name',
            'initials',
            'first_name',
            'last_name',
            'gender',
            'bsn',
            'birth_date',
            'birth_place',
            'birth_country',
            'nationality',
            'addresses',
            'driverslicenses',
            'dangers',
            'registrations',
            'signals',
        )


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer



