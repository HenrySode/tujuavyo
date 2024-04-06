from requests import Response
from rest_framework import generics, status
from . models import Category, Book, Course, Question
from .serializers import CategorySerializer, BookSerializer, CourseSerializer, QuestionSerializer
from rest_framework.views import APIView 

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def delete(self, request, *args, **kwargs):
        object = Category.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def delete(self, request, *args, **kwargs):
        object = Book.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def delete(self, request, *args, **kwargs):
        object = Course.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def delete(self, request, *args, **kwargs):
        object = Question.objects.all()
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



