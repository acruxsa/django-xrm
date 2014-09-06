from django.conf.urls import patterns, include, url


urlpatterns = patterns('frontend.views',
    # Examples:
    # url(r'^$', 'django_xrm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'person_list', name='person_list'),
)