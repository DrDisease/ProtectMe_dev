from rest_framework import serializers
from.models import TweetTopic, Tweet
#from django.contrib.auth.modes import User

class TweetTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetTopic
        fields = '__all__'
        #topic name input
        extra_kwargs = {'name':{'required':True}}

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
        #url input
        extra_kwargs = {'url':{'required':True}}
