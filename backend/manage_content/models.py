from django.db import models
from backend.discort_bot.models import Tag, SoundClip


class Collection(models.Model):
    name = models.TextField()
    sound_clips = models.ManyToManyField(SoundClip)

    class Meta:
        ordering = ['name']

    def str(self):
        return self.name