from rest_framework import serializers
from backend.manage_user import models


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['id', 'playlists', 'guilds']


class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Guild
        fields = ['id', 'name']
