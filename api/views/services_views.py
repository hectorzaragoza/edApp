from rest_framework import generics
from ..models.services import Services
from ..serializers import ServicesSerializer

class Services(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer