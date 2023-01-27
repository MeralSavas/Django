from rest_framework.viewsets import ModelViewSet
from .models import Car, Reservation
from .serializers import CarSerializer
from .permissions import IsStaffOrReadOnly

from django.db.models import Q



class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsStaffOrReadOnly,) #[isStaffOrReadOnly]

    def get_queryset(self):
        #staff ise hepsini 
        if self.request.user.is_staff:
            queryset = super().get_queryset()
        #client(musteri ise) sadece musait olanlari gorsun
        else:
            queryset = super().get_queryset().filter(availability=True)

        #sadece sectigi tarih araligindaki musait araclari gorsun
        #bunun icin frontend tarafindan gonderilen parametreleri yakaliyoruz
        start = self.request.query_params.get('start') # 8 9 10 11 12 13
        # print(start)
        end = self.request.query_params.get('end')# 10
        # print(end)

        condition1 = Q(start_date__lt=end) #less than 9
        condition2 = Q(end_date__gt=start) # greater than 11

        # not_available = Reservation.objects.filter(
        #     start_date__lt=end, end_date__gt=start
        # ).values_list('car_id', flat=True)  # [1, 2]

        not_available = Reservation.objects.filter(
            condition1 & condition2
        ).values_list('car_id', flat=True) # [1, 2]

        queryset = queryset.exclude(id__in=not_available)

        return queryset



