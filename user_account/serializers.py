from rest_framework import serializers
from  .models import User, Category, Expert, Message


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','is_expert', 'created']
        

class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = ['id', 'name', 'username', 'location', 'short_intro', 'bio', 'avatar','call_button', 'sms_button', 'whatsap_button']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'name', 'email', 'subject','body','is_read','created']
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()