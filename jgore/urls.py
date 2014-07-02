from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'news.views.show', name='home'),
    url(r'^news$', 'news.views.show', name='news'),
    url(r'^kontakt$', 'contact.views.contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
)
