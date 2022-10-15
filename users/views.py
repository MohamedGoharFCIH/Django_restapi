from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
from users.models import MyUser
from .serializers import RegistrationSerializer, MyUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser

import jwt
from  myproject.settings import SIMPLE_JWT


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

      
class LoginView(APIView):
    def post(self, request):
        if 'phone_number' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        print(phone_number, password)
        user = authenticate(request, phone_number=phone_number, password=password)
         
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

      
class StatusView(APIView):
    def post(self, request):
            if 'phone_number' not in request.data or 'status' not in request.data or 'auth-token' not in request.data:
                return Response({'msg': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = MyUser.objects.get(phone_number=request.POST['phone_number'])
            if user is  None or  status =="401":
                return  Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            user_serializer = MyUserSerializer(user)
            
            token = request.POST['auth-token']
            print( SIMPLE_JWT)
            decoded_token = jwt.decode(
                token,
                SIMPLE_JWT['SIGNING_KEY'],
                algorithms=[SIMPLE_JWT['ALGORITHM']],
                options={"verify_signature": False}  
            )
            if decoded_token is not None and  decoded_token["user_id"] == user_serializer.data["id"]  and request.POST['phone_number']!="401":
                return Response({'user':user_serializer.data , "token": decoded_token}, status=status.HTTP_200_OK)

            return  Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


            
           
            
                
