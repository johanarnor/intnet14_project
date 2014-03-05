from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dirr_activities.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('users.urls', namespace='users')),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^activities/', include('activities.urls', namespace='activities')),
)
