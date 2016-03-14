from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lfp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^popular/',include('popular.urls',namespace="popular")),
    url(r'^',include('home.urls',namespace="home")),
    url(r'^featured/',include('featured.urls',namespace="featured")),
    url(r'^contact-us/',include('contact.urls',namespace="contact")),
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


