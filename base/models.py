from django.db import models


# Create your models here.

class ArticleData(models.Model):
  id=models.IntegerField(default=0,primary_key=True)
  title=models.CharField(max_length=100)
  desc=models.TextField()

class NewsData(models.Model):
  id=models.IntegerField(default=0,primary_key=True)
  title=models.CharField(max_length=100)
  author=models.CharField(max_length=100)
  date=models.CharField(max_length=100)
  content=models.TextField(max_length=100)

class EventsData(models.Model):
  id=models.IntegerField(default=0,primary_key=True)
  name=models.CharField(max_length=100)
  date=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  type=models.CharField(max_length=100)

