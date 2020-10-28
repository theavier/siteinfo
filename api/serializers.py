from rest_framework import serializers

from .models import Site, Framework, Provider, GeoInfo

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('name', 'url')

class FrameworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Framework
        fields = ('site', 'app', 'type', 'ver', 'date')

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('site', 'provider', 'ip', 'source', 'date')

class GeoInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeoInfo
        fields = ('site', 'city', 'countrycode', 'country', 'latitude', 'longitude', 'date')

