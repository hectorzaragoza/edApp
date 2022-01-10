from rest_framework import generics
from rest_framework.response import Response
from ..models.services import Services
from ..serializers import ServicesSerializer

class AllServices(generics.ListCreateAPIView):
    IsAuthenticated = ()
    permission_classes = ()
    serializer_class = ServicesSerializer
    def get(self, request):
        """Index request"""
        # Get all the services offered:
        services = Services.objects.all()
        # Run the data through the serializer
        print('These are my existing services', services)
        data = ServicesSerializer(services, many=True).data
        print('data', data)
        return Response({ 'services': data })