from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/game/<int:game_id>', views.gamedetail, name='gamedetail'),
    path('/player/<int:player_id>', views.playerdetail, name='playerdetail')
    path('/gameentry', views.entry, name='entry')
]
