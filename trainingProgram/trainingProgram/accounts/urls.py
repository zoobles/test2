from django.conf.urls import include, url, patterns
from .views import register

urlpatterns = patterns('',
                       url(r'^$', 'accounts.views.register', name='register'),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': '/home/dev/trainingProgram/static'}),

)
