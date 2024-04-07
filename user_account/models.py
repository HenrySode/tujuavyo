from django.utils import timezone
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username = None, password = None):
        #Validate with email
        if not email:
            raise ValueError("Email is required")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=500, blank=True, null=True, unique=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def __str__(self):
        return self.username
    #functions to permit admin
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True

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
    
    
