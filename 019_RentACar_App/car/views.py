from rest_framework.viewsets import ModelViewSet
from .models import Car, Reservation
from .serializers import CarSerializer



class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = None




