from django.conf.urls import patterns, include, url
from django.contrib import admin
from home_page.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bennett_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home)
)
