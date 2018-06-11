"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
    
from django.conf.urls import *

from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from ShareHouse.views import search_list
from ShareHouse.views import show
from ShareHouse.views import H_show
from ShareHouse.views import index
from ShareHouse.views import home
from ShareHouse.views import learn
from ShareHouse.views import learn1
from ShareHouse.views import shadd
from ShareHouse.views import scene_update
from ShareHouse.views import ajax_list
from ShareHouse.views import learn3
from ShareHouse.views import add
from ShareHouse.views import share_house
from ShareHouse.views import H_add
from ShareHouse.views import house_info
from ShareHouse.views import homepage
from ShareHouse.views import AuthorCreate
from ShareHouse.views import ProfileUpdateView
from ShareHouse.views import p_list
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import CreateView
from ShareHouse.views import gupiao

urlpatterns = [
    url(r'^gupiao/$', gupiao),
    url(r'^$', home),
    url(r'^accounts/', include('users.urls') ),
    url(r'^admin/', include(admin.site.urls)),
   
    url(r'^index/$', index),
    url(r'^p_list/$', p_list),
    
    url(r'^H_list/$', search_list),
    url(r'^learn/$', learn),
    url(r'^learn1/$', learn1),
    url(r'^shadd/$', shadd),
    url(r'^scene_update/$',scene_update),
    url(r'^ajax_list/$',ajax_list),
    url(r'^learn3/$', learn3),
    url(r'^add/$', add),
    url(r'^share_house/$', share_house),
    url(r'^H_add/$', H_add),
    url(r'^home/$', home),
    url(r'^H_show/$', H_show),
    #url(r'^media\/(?P</media/photos>.*)$', show),
            url(r'^show/$', show),
    url(r'^author/$', AuthorCreate.as_view()),
    url(r'^p_update/$',ProfileUpdateView.as_view()),
    url(r'^house_info/$', house_info),
    url(r'^homepage/$', homepage),
   
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Website/media/photos'}), 
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )

