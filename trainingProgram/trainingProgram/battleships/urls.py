from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
              url(r'place/(?P<gameId>\d+)', 'battleships.views.placeShips', name='play'),
              url(r'shoot/(?P<gameId>\d+)', 'battleships.views.shoot', name='play'),
              url(r'(?P<gameId>\d+)', 'battleships.views.lobby', name='play')
)
