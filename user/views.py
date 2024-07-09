from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.
class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post (self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Registered Successfully"},status=status.HTTP_200_OK)
        Response(serializer.errors)    

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username,password= password)

        if user is not None:
            access =  AccessToken.for_user(user)
            return Response({
                'refresh': str(access),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)