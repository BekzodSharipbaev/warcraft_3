from django.urls import path

from .views import *

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('screenshots/', ScreenshotsPageView.as_view(), name='screenshots'),
    path('videos/', VideosPageView.as_view(), name='videos'),
    path('videos/cinematics/', CinematicsVideosPageView.as_view(), name='cinematics'),
    path('videos/game_process/',
         GameProcessVideosPageView.as_view(), name='game_process'),
    path('audios/', AudiosPageView.as_view(), name='audios'),
    path('audios/musics/', MusicAudiosPageView.as_view(), name='musics'),
    path('audios/character_replicas/',
         CharacterReplicasPageView.as_view(), name='character_replicas'),
    path('about/', AboutPageView.as_view(), name='about'),
]
