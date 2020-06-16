from django.db import models



# Create your models here.

class TweetTopic(models.Model):
    tweetID = models.IntegerField()
    feeling = models.TextField(max_length=None)
    feelingFinal = models.TextField(max_length=None)
    feelingNegative = models.DecimalField(max_digits=2, decimal_places=2)
    feelingPositive = models.DecimalField(max_digits=2, decimal_places=2)     
    averageLikes = models.IntegerField(max_length=None)
    averageRetweets = models.IntegerField(max_length=None)
    averageComments = models.IntegerField(max_length=None)
    averageProfanity = models.DecimalField(max_digits=2, decimal_places=2)
    keywords = models.TextField(max_length=None)

class Tweet(models.Model):
    tweetID = models.IntegerField()
    url = models.URLField()
    imageUrl = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    imageInfo=models.TextField(max_length=None)
