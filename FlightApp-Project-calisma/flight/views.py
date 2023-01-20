from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FlightSerializer
from .models import Flight
from rest_framework.permissions import IsAdminUser
from .permissions import IsStafforReadOnly

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsStafforReadOnly,)
