from django.db import models
from django.contrib.auth.models import User

class Advertisement(models.Model):
    titleRu = models.TextField(null=True, blank=True)
    titleUz = models.TextField(null=True, blank=True)
    hashCode = models.FileField(upload_to='advertisements', null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ("-date",)

class News(models.Model):
    descriptionRu = models.TextField(null=True, blank=True)
    descriptionUz = models.TextField(null=True, blank=True)
    hashCode = models.FileField(upload_to='news', null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-date",)

class Accountants(models.Model):
    textRu = models.TextField(null=True, blank=True)
    textUz = models.TextField(null=True, blank=True)
    reportAttachHashCode = models.FileField(upload_to='accountants', null=True, blank=True)
    accountantAttachHashCode = models.FileField(upload_to='accountants', null=True, blank=True)



class Tenders(models.Model):
    titleRu = models.TextField(null=True, blank=True)
    titleUz = models.TextField(null=True, blank=True)
    hashCode = models.FileField(upload_to='tenders', null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    finishedDate = models.DateField(null=True, blank=True)



class Nouns(models.Model):
    descriptionRu = models.TextField(null=True, blank=True)
    descriptionUz = models.TextField(null=True, blank=True)
    hashCode = models.FileField(upload_to='news', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ("-date",)