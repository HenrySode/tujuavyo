from django.contrib import admin
from .models import Category, Expert, User, Message


admin.site.register(Category)
admin.site.register(Expert)
admin.site.register(User)
admin.site.register(Message)
