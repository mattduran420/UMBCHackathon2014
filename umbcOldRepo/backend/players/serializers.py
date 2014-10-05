from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class PlayerSerializer(serializers.Serializer):
    user = UserSerializer()
    username = serializers.CharField()
    school = serializers.CharField()
    permalink = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()