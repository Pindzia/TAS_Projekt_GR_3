from django.conf.urls import patterns, include, url
from django.contrib import admin
from books import utils

admin.autodiscover()

# URLS - tutaj zamieszczamy urle do poszczegolnych podstron/aplikacji serwisu.


urlpatterns = patterns('',

    url(r'^$', 'books.views.home', name='home'), # Strona glowna.

    # url(r'^admin/', include(admin.site.urls)),
)

