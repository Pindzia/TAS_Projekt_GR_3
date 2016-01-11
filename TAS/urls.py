from django.conf.urls import patterns, include, url

# URLS - tutaj zamieszczamy urle do poszczegolnych podstron/aplikacji serwisu.

urlpatterns = patterns('',

    url(r'^$', 'books.views.home', name='home'), # Strona glowna bez parametru.
    url(r'^test/$', 'books.views.test', name='test'), # Strona testowa.
    url(r'^(.+)/$', 'books.views.home', name='home'), # Strona glowna z parametrem.
    # url(r'^admin/', include(admin.site.urls)),
)
