from django.contrib import admin

# Register your models here.
from .models import TweetTopic, Tweet


admin.site.register(TweetTopic)
admin.site.register(Tweet)