#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
	author = models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	content = models.TextField()

class FollowRelation(models.Model):
	user     = models.CharField(max_length=60)
	follower = models.CharField(max_length=60)

class msg(models.Model):
	user    = models.CharField(max_length=60)
	msgid   = models.IntegerField()
	msgtype = models.CharField(max_length=60)
