from rest_framework import serializers
from .models import (Films,Review,TokensUser)
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = ['pk', 'name', 'type', 'description', 'author','image_url', 'banner_url']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class ReviewSeriaizer(serializers.ModelSerializer):
    user = UserSerializer()
    film = FilmsSerializer()
    class Meta:
        model = Review
        fields = ["pk","user","film","ranged","critic","film"]


class TokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokensUser
        fields = ["pk","user_fk","expiration","token"]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email
        return token
    
