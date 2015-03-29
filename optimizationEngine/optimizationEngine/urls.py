from django.conf.urls import patterns, include, url
from django.contrib import admin
from engineApp import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'optimizationEngine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^scanTarget/$', views.scanTarget),
)
