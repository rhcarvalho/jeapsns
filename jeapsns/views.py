#coding=utf-8
from django.http import HttpResponse
from django.contrib.auth.forms import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from jeapsns.models import *
from jeapsns.forms import *


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
		form = postForm()
		post_all = post.objects.filter(author=request.user.username)
		if request.method == 'POST':
			new_post = post(author=request.user.username,content = request.POST['content'])
			new_post.save()
		return render_to_response("index.html",{'name':request.user.username,'form':form,\
			"post_all":post_all},context_instance=RequestContext(request))
	return HttpResponseRedirect("/accounts/login/?next=/")
