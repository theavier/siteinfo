from django.db import models
from datetime import datetime

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
    date = models.DateField(default=datetime.today())
    def __str__(self):
        return self.app