#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
	author = models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	content = models.TextField()

