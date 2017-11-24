from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth.models import User
#

 #Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')