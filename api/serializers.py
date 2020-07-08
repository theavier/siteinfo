from rest_framework import serializers

from .models import Site, Framework

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('name', 'url')

class FrameworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Framework
        fields = ('site', 'app')