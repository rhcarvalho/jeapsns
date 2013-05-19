#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    author = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return u"Post by {}, on {}: {}".format(self.author, self.created, self.content).encode("utf-8")
        
    def __unicode__(self):
        return u"Post by {}, on {}: {}".format(self.author, self.created, self.content)

class FollowRelation(models.Model):
	user     = models.CharField(max_length=60)
	follower = models.CharField(max_length=60)

class msg(models.Model):
	user    = models.CharField(max_length=60)
	msgid   = models.IntegerField()
	msgtype = models.CharField(max_length=60)
