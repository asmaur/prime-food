from rest_framework import viewsets
from prime.models import Address

from prime.v1.serializers import (
    AddressSerializer
)
# Create your views here.
# post, get, update


class AddressViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
