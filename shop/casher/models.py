from django.db import models

# Create your models here.
from django.utils import timezone


class Revealed(models.Model):
    time = models.TimeField(auto_now=True, auto_now_add=False)
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=250)
    eye = models.CharField(max_length=250)
    lens = models.CharField(max_length=250)
    given = models.CharField(max_length=20)
    reminder = models.CharField(max_length=20)
    docName = models.CharField(max_length=250)
    revealDate = models.DateField(default=timezone.now)
    rSphN = models.CharField(max_length=20)
    rCylN = models.CharField(max_length=20)
    rAxisN = models.CharField(max_length=20)
    lSphN = models.CharField(max_length=20)
    lCylN = models.CharField(max_length=20)
    lAxisN = models.CharField(max_length=20)
    rSphF = models.CharField(max_length=20)
    rCylF = models.CharField(max_length=20)
    rAxisF = models.CharField(max_length=20)
    lSphF = models.CharField(max_length=20)
    lCylF = models.CharField(max_length=20)
    lAxisF = models.CharField(max_length=20)
    paName = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    delStatus = models.BooleanField(default=False)
    ann = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time']


class Total(models.Model):
    total = models.CharField(max_length=250)


class Store(models.Model):
    time = models.TimeField(auto_now=True, auto_now_add=False)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='media', blank=True, null=True, max_length=150, default='glasses.jpg')
    quan = models.CharField(max_length=50)

    class Meta:
        ordering = ['-time']
