from django.db import models

class MChild(models.Model):
    name=models.TextField()
    gender=models.TextField()
    height=models.FloatField()
    age=models.IntegerField()
    ageNow=models.IntegerField()
    alldressing=models.TextField()
    occrAdd=models.TextField()
    occrDate=models.DateField
    writngTarget=models.TextField()