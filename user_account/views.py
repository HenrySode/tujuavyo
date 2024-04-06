from tokenize import Token
from django.shortcuts import render
from requests import Response
from rest_framework import generics, status
from . models import User, Category, Expert, Message
from .serializers import UserSerilizer, LoginSerializer,  CategorySerializer, ExpertSerializer, MessageSerializer
from rest_framework.views import APIView 

#User API login and registration
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilizer
    
    def delete(self, request, *args, **kwargs):
        object = User.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    
class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilizer
    lookup_field = "pk"

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            #User Authentication
            # user = authenticate(request, email=email, password=password)
            # if user:
            #     token, _ = Token.objects.get_or_create(user=user)
            #     return Response({'token': token.key}, status=status.HTTP_200_OK)
            # else:
            #     return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#CRUD Category API
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def delete(self, request, *args, **kwargs):
        object = Category.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
#CRUD Expert API
class ExpertListCreate(generics.ListCreateAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    
    def delete(self, request, *args, **kwargs):
        object = Expert.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ExpertRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expert.objects.all()     
    serializer_class = ExpertSerializer
    lookup_field = "pk"

#CRUD Message API
class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def delete(self, request, *args, **kwargs):
        object = Message.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class MessageRetrieveUpdateDestroy(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'pk'