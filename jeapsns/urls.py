from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeapsns.views.home', name='home'),
    # url(r'^jeapsns/', include('jeapsns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
	(r'^accounts/register/$', 'jeapsns.views.register'),
	(r'^accounts/user/$', 'jeapsns.views.user_list'),
	(r'^$', 'jeapsns.views.index'),
	(r'^save$', 'jeapsns.views.save'),
	(r'^follow/$', 'jeapsns.views.follow'),
)
