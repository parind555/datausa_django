from rest_framework import serializers
from models import User, UserRequest


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('user_name', 'email')


class UserRequestSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserRequest
        fields = ('user', 'request_id', 'update_time', 'status', 'data')