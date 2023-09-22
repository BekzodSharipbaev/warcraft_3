from django.views.generic import TemplateView, ListView

from .models import *

# Create your views here.


class StartPageView(TemplateView):
    template_name = 'warcraft_app/start_page.html'
    extra_context = {'title': 'Стартовая страница'}


class ScreenshotsPageView(ListView):
    model = Screenshots
    template_name = 'warcraft_app/screenshots_page.html'
    context_object_name = 'screenshots'
    extra_context = {'title': 'Скриншоты'}


class VideosPageView(TemplateView):
    template_name = 'warcraft_app/videos_page.html'
    extra_context = {'title': 'Видео'}


class CinematicsVideosPageView(ListView):
    model = Videos
    template_name = 'warcraft_app/cinematics.html'
    context_object_name = 'videos'
    extra_context = {'title': 'Синематики'}

    def get_queryset(self):
        return self.model.objects.filter(category__title='cinematics')


class GameProcessVideosPageView(ListView):
    model = Videos
    template_name = 'warcraft_app/game_process.html'
    context_object_name = 'videos'
    extra_context = {'title': 'Игровой процесс'}

    def get_queryset(self):
        return self.model.objects.filter(category__title='game_process')


class AudiosPageView(TemplateView):
    template_name = 'warcraft_app/audios_page.html'
    extra_context = {'title': 'Аудио'}


class MusicAudiosPageView(ListView):
    model = Audios
    template_name = 'warcraft_app/music.html'
    context_object_name = 'audios'
    extra_context = {'title': 'Музыка'}

    def get_queryset(self):
        return self.model.objects.filter(category__title='music')


class CharacterReplicasPageView(ListView):
    model = Audios
    template_name = 'warcraft_app/character_replicas.html'
    context_object_name = 'audios'
    extra_context = {'title': 'Реплики персонажей'}

    def get_queryset(self):
        return self.model.objects.filter(category__title='character_replicas')


class AboutPageView(TemplateView):
    template_name = 'warcraft_app/about_page.html'
    extra_context = {'title': 'Об игре'}
