from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions

from .models import Place, Booking
from .serializers import PlaceSerializer, BookingSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = (permissions.IsAuthenticated,)

