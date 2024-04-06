from django.utils import timezone
import uuid
from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    
    
    
    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    is_expert = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique = True,
                          primary_key = True, editable = False)
    
    def __str__(self):
        return self.title

class Expert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='expert_profile')
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    call_button = models.CharField(max_length=200, blank=True, null=True)
    sms_button = models.CharField(max_length=200, blank=True, null=True)
    whatsap_button = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.username
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete = models.SET_NULL, blank = True, null = True)
    recipient =  models.ForeignKey(User, on_delete = models.SET_NULL, blank = True, null = True, related_name = 'messages')
    name = models.CharField(max_length = 200, null = True, blank = True)
    email = models.EmailField(max_length = 200, null = True, blank = True)
    subject = models.CharField(max_length = 200, null = True, blank = True)
    body = models.TextField()
    is_read = models.BooleanField(default = False, null = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique = True,
                          primary_key = True, editable = False)
    
    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['is_read', '-created']
    
    
