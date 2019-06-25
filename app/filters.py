import coreapi
from rest_framework.filters import BaseFilterBackend

from app.abstractions import Point

__all__ = ['LatLongFilter']


def get_latitude(query_params: dict) -> str or None:
    return query_params.get('lat') or query_params.get('y') or query_params.get('latitude')


def get_longitude(query_params: dict) -> str or None:
    return query_params.get('long') or query_params.get('x') or query_params.get('longitude')


class LatLongFilter(BaseFilterBackend):
    def get_schema_fields(self, view):
        # noinspection PyArgumentList
        return [
            coreapi.Field(name="y", description="Latitude", required=False, location='query'),
            coreapi.Field(name="x", description="Longitude", required=False, location='query'),
            coreapi.Field(name="lat", description="Latitude", required=False, location='query'),
            coreapi.Field(name="long", description="Longitude", required=False, location='query'),
            coreapi.Field(name="latitude", description="Latitude", required=False, location='query'),
            coreapi.Field(name="longitude", description="Longitude", required=False, location='query'),
        ]

    def filter_queryset(self, request, queryset, view):
        latitude = get_latitude(request.query_params)
        longitude = get_longitude(request.query_params)
        if not (latitude and longitude):
            return queryset

        # Creating another queryset so it's possible to use it as a queryset throughout the request (other filters)
        point = Point(float(longitude), float(latitude))
        polygons_ids = [polygon.id for polygon in queryset.only('id', 'points') if polygon.contains(point)]
        return queryset.filter(id__in=polygons_ids)
