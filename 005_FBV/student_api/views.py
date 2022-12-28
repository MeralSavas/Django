from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view() # default GET
def home(request):
    return Response({'home': 'This is home page...'})


# http methods --------->
# - GET (DB den veri cagirma, public)
# - POST (DB de degisiklik yapma, create, private)
# - PUT (DB de kayit degikligi, private butun datayi gondermeniz gerekir)
# - DELETE (DB de kayit silme)
# - PATCH (kismi update)

@api_view(['GET']) 
def students_list(request):
    students =Student.objects.all()
    # print(students)
    serializer = StudentSerializer(students, many=True)
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)

@api_view(['POST']) 
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Student created successfully....'
        
        }
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)

@api_view(['GET'])
def student_detail(request, pk):
   
    student = get_object_or_404(Student, id=pk)
    # student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Student updated successfully....'
        
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)


@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(student, id=pk)
    student.delete()
    message = {
        "message": f'Student deleted successfully....'
        
        }
    return Response(message)




    #############################################################

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)