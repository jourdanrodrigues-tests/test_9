from rest_framework import serializers

from app.models import Provider, ServiceArea


class PointsSerializer(serializers.ListField):
    child = serializers.ListField(
        child=serializers.FloatField(),
        min_length=2,
        max_length=2,
        allow_empty=False,
    )

    def __init__(self, *args, **kwargs):
        kwargs['min_length'] = 3
        kwargs['allow_empty'] = False
        super().__init__(*args, **kwargs)


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            'id',
            'name',
            'email',
            'language',
            'currency',
            'phone_number',
        ]


class ServiceAreaSerializer(serializers.ModelSerializer):
    points = PointsSerializer(write_only=True)

    class Meta:
        model = ServiceArea
        fields = [
            'id',
            'name',
            'price',
            'points',
            'provider',
        ]
