from persons.models import Person, DriversLicense, DangerClass, Registration
from rest_framework import routers, serializers, viewsets


from myapp.models import Purchase
from myapp.serializers import PurchaseSerializer
from rest_framework import generics


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


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = ('id', 'url', 'person', 'title', 'mk', 'role', 'type', 'date')


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    driverslicenses = DriverslicenseSerializer(many=True)
    dangers = DangerClassSerializer(many=True)
    registrations = RegistrationSerializer(many=True)

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
            'driverslicenses',
            'dangers',
            'registrations',
        )


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonList(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Person.objects.all()
        keno = self.request.query_params.get('keno', None)
        if keno is not None:
            queryset = queryset.filter(keno=keno)
        return queryset