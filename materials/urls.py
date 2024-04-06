from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreate.as_view(), name='categories'),
    path('books/', views.BookListCreate.as_view(), name='books'),
    path('courses/', views.CourseListCreate.as_view(), name='courses'),
    path('questions/', views.QuestionListCreate.as_view(), name='questions'),
]