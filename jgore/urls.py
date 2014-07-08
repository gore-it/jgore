from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'news.views.show', ),
    url(r'^news$', 'news.views.show', ),
    url(r'^projekty$', 'projects.views.show', ),
    url(r'^edukacja/(?P<article_id>\d+)/$', 'education.views.article', ),
    url(r'^edukacja$', 'education.views.show', ),
    url(r'^forum$', 'forum.views.show', ),
    url(r'^kontakt$', 'contact.views.contact', ),

    url(r'^admin/', include(admin.site.urls)),
)
