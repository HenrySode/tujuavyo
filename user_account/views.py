
from requests import Response
from rest_framework import generics, status
from . models import User, Category, Expert, Message
from .serializers import UserSerializer, LoginSerializer,  CategorySerializer, ExpertSerializer, MessageSerializer
from rest_framework.views import APIView 


from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken



#User API login and registration
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def delete(self, request, *args, **kwargs):
        object = User.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    
class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    
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
    
class LoginApiView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer_data = UserSerializer(user).data
        token = RefreshToken.for_user(user)
        data = {
            "refresh":str(token),
            "access":str(token.access_token),
            "user": {
                'is_admin': user.is_admin,
                'data':serializer_data
            }
        }
        return Response(data, status=status.HTTP_200_OK)