from django.conf.urls import patterns, include, url
from testApi.api import FoodResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

food_resource = FoodResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'authApp.views.home', name='home'),
    # url(r'^authApp/', include('authApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    (r'^api/', include(food_resource.urls)),
    (r'^logged-in/$', 'testApi.views.user_creds'),
    (r'^auth/$', 'testApi.views.auth_approved'),
)