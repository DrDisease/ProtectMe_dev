from django.shortcuts import render
from rest_framework import viewsets,status
from . models import TweetTopic, Tweet
from . serializers import TweetTopicSerializer, TweetSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action


# Create your views here.
class TweetTopicViewSet(viewsets.ModelViewSet):
    queryset = TweetTopic.objects.all()
    serializer_class = TweetTopicSerializer
    permission_classes = (AllowAny)
    
    @action(methods=['POST'], detail=True)
    def getTweetT(self,request,pk=None):
        if 'topic' in request.data:
            # tweetID = request.data['tweetID']
            topicName = request.data['topic']
            feeling = request.data['average_feeling']
            averageLikes = request.data['average_likes']
            averageNegative = request.data['negative']
            averagePositive = request.data['positive']
            averageRetweets = request.data['average_retweets']
            averageComments = request.data['average_comments']
            averageProfanity = request.data['profanity']
            keywords =request.data['keywords']
            # If Topic on db
            try:
                topic.feeling = feeling
                topic.averageLikes = averageLikes
                topic.averageNegative = averageNegative
                topic.averagePositive = averagePositive
                topic.averageRetweets = averageRetweets
                topic.averageComments = averageComments
                topic.averageProfanity = averageProfanity
                topic.keywords = keywords
                topic.save()
                
                serializer = TweetTopicSerializer(topic,many=False)
                response = {'message':'Topic found','result':serializer.data}
                return Response(response, status = status.HTTP_200_OK)
            # Ask db for new
            except:

                topic = TweetTopic.objects.create(topic=topic)
                serializer = TweetTopicSerializer(topic,many=false)
                response = {'message':'New Topic Added','result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message':'Please enter a topic'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (AllowAny)