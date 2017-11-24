'''
serializers for API
'''
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _



class GetHotelsSerializer(serializers.Serializer):
    """smart spPayments serializer."""
    hotel_ids = serializers.CharField()
    extras = serializers.CharField()

    def validate(self, attrs):
        hotel_ids = attrs.get('hotel_ids')
        extras = attrs.get('extras')

        if not hotel_ids:
            raise serializers.ValidationError()
        return attrs

class GetHotelTypesSerializer(serializers.Serializer):
    """smart spPayments serializer."""
    languages = serializers.CharField()
    rows = serializers.CharField()

    def validate(self, attrs):
        languages = attrs.get('languages')
        rows = attrs.get('rows')

        if not rows:
            raise serializers.ValidationError()
        return attrs


class GetHotelFacilityTypesSerializer(serializers.Serializer):
    """smart spPayments serializer."""
    languages = serializers.CharField()
    rows = serializers.CharField()

    def validate(self, attrs):
        languages = attrs.get('languages')
        rows = attrs.get('rows')

        if not rows:
            raise serializers.ValidationError()
        return attrs