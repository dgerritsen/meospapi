from django.conf.urls import url, include, patterns
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from persons.serializers import PersonViewSet, PersonSignalViewSet, DriverslicenseViewSet, DangerClassViewSet, RegistrationViewSet, AddressViewSet
from vehicles.serializers import VehicleViewSet, VehicleSignalViewSet
from django.conf.urls import url
from django.contrib import admin

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'personsignals', PersonSignalViewSet)
router.register(r'driverslicense', DriverslicenseViewSet)
router.register(r'dangerclass', DangerClassViewSet)
router.register(r'registration', RegistrationViewSet)
router.register(r'address', AddressViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'vehiclesignals', VehicleSignalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
)) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)