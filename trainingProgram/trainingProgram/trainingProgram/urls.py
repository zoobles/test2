from django.conf.urls import include, url
from django.contrib import admin
from main.views import home
from django.contrib.auth.views import login
import django.contrib.auth.views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='main_home'),
]

# urlpatterns = ('',
#                        url(r'^admin/', include(admin.site.urls)),
#                        # url(r'^$', 'main.views.home', name='main_home'),
#                        # url(r'^register', include('accounts.urls'), name='register'),
#                        # url(r'^new_game', 'battleships.views.new_game', name='new_game'),
#                        # (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
#                        # {'document_root': '/home/dev/trainingProgram/static'}),
#                        # url(r'^game/', include('battleships.urls'), name='game'),
#                        # url(r'^games_list', 'battleships.views.games_list', name='placements'),
#                        # url(r'^lobby/', include('battleships.urls'), name='lobby'),
#                        # url(r'^login/$', 'accounts.views.auth_login', {'template_name': 'accounts/login.html'},
#                        #     name='login'),
#                        # url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': 'main_home'}),
# )
