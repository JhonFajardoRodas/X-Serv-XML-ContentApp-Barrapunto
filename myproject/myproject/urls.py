from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^update$', 'ContentApp_BarraPunto.views.mostrarTodo'),
    url(r'^(.*)$', 'ContentApp_BarraPunto.views.buscarPersona'),
)
