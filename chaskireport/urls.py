# coding: utf-8
from django.conf.urls import patterns, include, url
from webapp.views import *
from django.contrib import admin
from django.contrib.auth.views import login, logout
import settings
from django.conf.urls.static import static


#DJANGO REST FRAMEWORK
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chaskireport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
]