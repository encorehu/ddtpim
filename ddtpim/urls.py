from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ddtpim.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

try:
    from local_urls import *
    print 'local urls loaded'
except ImportError,e:
    print  e
    print 'local urls NOT loaded'
