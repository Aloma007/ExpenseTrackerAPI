from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Used create_user so the password gets hashed automatically
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class ExpenseSerializer(serializers.ModelSerializer):
    # Automatically tie the expense to the user holding the JWT
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Expense
        fields = ['id', 'user', 'amount', 'category', 'description', 'date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']