from . import views
from django.urls import path,include
from app import api
urlpatterns = [
 path('',views.home,name='index'),

 path('data/temperature',views.dht11,name='Data'),
 path('data/Last24',views.dht13,name='Last24'),

 path('data/graphe',views.dht12,name='Data'),

 path('api/list', api.Dlist, name='DHT11List'),
 path('api/post', api.Dhtviews.as_view(), name='DHT_post'),

 path('csv', views.exp_csv, name = 'exp-csv'),
 path('csv1', views.exp_csv1, name = 'exp-csv1'),

]