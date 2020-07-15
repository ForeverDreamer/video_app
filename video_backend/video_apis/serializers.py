from rest_framework import serializers

from.models import Place, Booking


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        # fields = '__all__'
        exclude = ('create_time', 'last_modified')


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        # fields = '__all__'
        exclude = ('create_time', 'last_modified')
