from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import TweetTopicViewSet, TweetViewSet

router = routers.DefaultRouter()
router.register('tweets',TweetViewSet)
router.register('tweetTopic',TweetTopicViewSet)

urlpatterns = [
    path('', include(router.urls))
]
