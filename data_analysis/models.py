from django.db import models

# Create your models here.
class accident_pie(models.Model):
    type_name = models.CharField(max_length=20)
    count = models.IntegerField()

class accident_bar(models.Model):
    company_name = models.CharField(max_length=20)
    count = models.IntegerField()

class event_pie(models.Model):
    type_name = models.CharField(max_length=20)
    count = models.IntegerField()

class event_bar(models.Model):
    company_name = models.CharField(max_length=20)
    count = models.IntegerField()