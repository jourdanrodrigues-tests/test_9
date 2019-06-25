from rest_framework import viewsets
from rest_framework.response import Response

from app.filters import LatLongFilter
from app.models import Provider, ServiceArea
from app.serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    filter_backends = [LatLongFilter]

    def list(self, request, *args, **kwargs):
        # This override performs the filtering after the pagination, since the latitude/longitude filter needs to
        # iterate over all objects.
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            page = self.filter_queryset(page)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
