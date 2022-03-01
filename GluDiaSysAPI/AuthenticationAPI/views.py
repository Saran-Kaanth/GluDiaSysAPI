from django.shortcuts import render
from .serializers import *
from rest_framework import generics,status
from rest_framework.response import Response
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class RegisterAPIView(generics.CreateAPIView):
    serializer_class=RegisterSerializer

    def post(self,request):
        print(request.data)
        serializer=self.serializer_class(data=request.data)
        # user_value=CustomUser.objects.check(email=request.data["email"])
        # print(user_value)
        if serializer.is_valid():
            serializer.save()
            user_data=serializer.data
            user=CustomUser.objects.get(email=user_data["email"])
            token=RefreshToken.for_user(user=user)
            token_2=token.access_token
            print(token)
            print(token_2)
            print(user_data)
            return Response(user_data,status=status.HTTP_201_CREATED)
        return Response({"message":"Check the Provided credentials","error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        # return Response({"message":"Email already exists"},status=status.HTTP_400_BAD_REQUEST)
