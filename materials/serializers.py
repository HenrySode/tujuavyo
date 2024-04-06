from rest_framework import serializers
from .models import Category, Book, Course, Question

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','created']
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','book_title','book_image', 'author_name', 'created' ]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','course_name', 'created']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer', 'option_one', 'option_two', 'option_three',]