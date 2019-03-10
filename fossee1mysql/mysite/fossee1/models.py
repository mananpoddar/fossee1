from django.db import models

class Caption(models.Model):
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField(blank=False)

class Images(models.Model):
    image = models.ImageField(upload_to='images/')

class manan(models.Model):
    title = models.CharField(max_length=80, blank=False)
