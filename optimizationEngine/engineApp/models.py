from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    ip = models.IPAddressField()
    point = models.PointField()
    objects = models.GeoManager()

class Target(models.Model):
    location = models.ForeignKey(Location)
    name = models.CharField(max_length=150)
    url = models.URLField()

class Server(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location)

class Scan(models.Model):
    date = models.DateTimeField('scan time')
    target = models.ForeignKey(Target)

class Asset(models.Model):
    name = models.CharField(max_length=1024)
    scan = models.ForeignKey(Scan)
    url = models.URLField()
    requestTime = models.DateTimeField()
    responseTime = models.DateTimeField()
    fileSize = models.PositiveIntegerField()
    httpStatus = models.SmallIntegerField()
    probeServer = models.ForeignKey(Server, related_name="probeServer")
    hostServer = models.ForeignKey(Server, related_name="hostServer")



