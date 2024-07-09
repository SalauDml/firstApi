from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer
from rest_framework import permissions
# Create your views here.

class StudentListEndpoint(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Post added successfully","data":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def update(self,instance,validated_data):
        print(vars(instance),"instance__dict__")
        instance.name = validated_data.get("name",instance.name)
        instance.email = validated_data.get("email",instance.email)
        instance.address = validated_data.get("address",instance.address)
        instance.save()
        return instance
    
    def delete(self,request,id):
        try:
            student = Student.objects.get(pk=id)
        except Student.DoesNotExist:
            raise Response({"error": "Student does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)