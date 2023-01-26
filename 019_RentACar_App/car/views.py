from rest_framework.viewsets import ModelViewSet
from .models import Car, Reservation
from .serializers import CarSerializer
from .permissions import IsStaffOrReadOnly



class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsStaffOrReadOnly,) #[isStaffOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(availability=True)
        start = self.request.query_params.get('start')
        print(start)
        end = self.request.query_params.get('end')
        print(end)

        return queryset



