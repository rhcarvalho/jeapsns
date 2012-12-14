#coding=utf-8
from django.http import HttpResponse
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
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
		msg_all = msg.objects.filter(user=request.user.username).order_by('-id')
		post_all = get_post_all(msg_all)
		if request.method == 'POST':
			new_post = post(author=request.user.username,content = request.POST['content'])
			new_post.save()
			m = msg (msgid=new_post.id,user=request.user.username)
			m.save()
			f = FollowRelation.objects.filter(follower=request.user.username)
			for n in f:
				m = msg(msgid=new_post.id,user=n.user)
				m.save()
		return render_to_response("index.html",{'name':request.user.username,'form':form,\
			"post_all":post_all},context_instance=RequestContext(request))
	return HttpResponseRedirect("/accounts/login/?next=/")

def user_list(request):
	if request.user.is_authenticated():
		u_all = User.objects.all()
		user_all = get_user_follows(request,u_all)
		return render_to_response('user.html',{'user_all':user_all},context_instance=RequestContext(request))

	return HttpResponseRedirect("/accounts/login/?next=/")

def get_user_follows(request,u_all):
	for user_all in u_all:
		follow = get_follow(request,user_all.username)
		user_all.follow = follow
		yield user_all


def get_follow(request,username):
	try:
		follow = FollowRelation.objects.get(user=request.user.username,follower=username)
		return follow
	except:
		return None

def get_post_all(msg_all):
	for m in msg_all:
		post_all = get_post(m.msgid)	
		yield post_all

def get_post(msgid):
	p = post.objects.get(id=msgid)
	return p

def follow(request):
	if 'username' in request.GET:
		username = request.GET['username']
		f = FollowRelation(user=request.user.username,follower=username)
 		f.save()
	return HttpResponseRedirect("/accounts/user")
