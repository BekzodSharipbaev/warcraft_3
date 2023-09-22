from email.policy import default
from unicodedata import category
from django.db import models
from django.forms import ImageField
from django.urls import reverse

# Create your models here.


class Screenshots(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    screenshot = models.ImageField(upload_to='screenshots/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('screenshot', kwargs={'screenshot_slug': self.slug})


VIDEOS_CATEGORY = [
    ('cinematics', 'Cinematics'),
    ('game_process', 'Game Process'),
]


class VideosCategory(models.Model):
    title = models.CharField(
        max_length=255, choices=VIDEOS_CATEGORY, default='cinematics')

    def __str__(self):
        return self.title


class Videos(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    video = models.FileField(upload_to='videos/')
    category = models.ForeignKey(VideosCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video', kwargs={'video_slug': self.slug})


AUDIOS_CATEGORY = [
    ('music', 'Music'),
    ('character_replicas', 'Replicas of Character'),
]


class AudiosCategory(models.Model):
    title = models.CharField(
        max_length=255, choices=AUDIOS_CATEGORY, default='music')

    def __str__(self):
        return self.title


class Audios(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    audio = models.FileField(upload_to='audios/')
    category = models.ForeignKey(AudiosCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('audio', kwargs={'audio_slug': self.slug})
