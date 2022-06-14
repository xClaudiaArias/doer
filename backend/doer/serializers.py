from rest_framework import serializers
from doer.models import ToDo, User

class toDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'user_id', 'title', 'category', 'due_date', 'description', 'completed', 'created', 'updated')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'created')