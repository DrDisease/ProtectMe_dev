from rest_framework import serializers
from.models import Video, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        extra_kwargs  = {'url': {'required':True}}

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ('id','stars','user','video','comments')


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username','password')
    extra_kwargs = {'password':{'write_only':True,'required':True}}

    def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      print(user)
      Token.objects.create(user=user)
      return user