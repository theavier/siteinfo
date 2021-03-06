from django.db import models
from django.utils import timezone

class Site(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Framework(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    app = models.CharField(max_length=100)
    ver = models.CharField(max_length=100, default="N/A")
    type = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.app


class Provider(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    provider = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.provider


class GeoInfo(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    countrycode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.country
