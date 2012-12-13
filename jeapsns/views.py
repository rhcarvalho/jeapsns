#coding=utf-8
from django.contrib.auth.forms import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def register(request):
	form = UserCreationForm()
	if request.method == 'GET':
		return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
        	if form.is_valid():
            		new_user = form.save()
            		return HttpResponseRedirect("/")

def index(request):
	if request.user.is_authenticated():
		return render_to_response("index.html",{'name':request.user.username})
	return HttpResponseRedirect("/accounts/login/")
