from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

class webpage(models.Model):
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField(max_length=200)

class Access_records(models.Model):
    name=models.ForeignKey(webpage, on_delete=models.CASCADE)
    age=models.DateField()