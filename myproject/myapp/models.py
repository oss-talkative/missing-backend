from django.db import models

class MChild(models.Model):
    name=models.TextField(null=True)
    gender=models.TextField(null=True)
    height=models.FloatField(null=True)
    age=models.IntegerField(null=True)
    ageNow=models.IntegerField(null=True)
    alldressing=models.TextField(null=True)
    occrAdd=models.TextField(null=True)
    occrDate=models.DateField(null=True)
    writngTarget=models.TextField(blank=True)

    def __str__(self):
        return self.name
