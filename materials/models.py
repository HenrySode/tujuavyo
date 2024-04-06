import uuid
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique = True,
                          primary_key = True, editable = False)

    def __str__(self):
        return self.title

class Book(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='book')
    book_title = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to='images/', blank=True, null=True)
    author_name = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique = True,
                          primary_key = True, editable = False)
   
    def __str__(self):
        return self.book_title
    

class Course(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='course')
    course_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique = True,
                          primary_key = True, editable = False)
    
    def __str__(self):
        return self.course_name
    

class Question(models.Model):
    course = models.ForeignKey(Course, max_length=100, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.IntegerField()
    option_one = models.CharField(max_length=100, blank=True)
    option_two = models.CharField(max_length=100, blank=True)
    option_three = models.CharField(max_length=100, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique = True,
                          primary_key = True, editable = False)
    
    def __str__(self):
        return self.question



