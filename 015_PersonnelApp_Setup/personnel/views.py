from .models import Department, Personnel
from .serializers import DepartmentSerializer, PersonnelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStafforReadOnly

class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated, IsStafforReadOnly]
    

class PersonnelListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    permission_classes = [IsAuthenticated, IsStafforReadOnly]
    # permission_classes = [IsAuthenticated]
