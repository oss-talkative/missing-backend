from django.db import models

class MChild(models.Model):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    name=models.TextField(null=True, blank=True)
    gender=models.CharField(choices=GENDER_CHICES, max_length=10, null=True, blank=True)
    height=models.FloatField(null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    ageNow=models.IntegerField(null=True, blank=True)
    alldressing=models.TextField(null=True, blank=True)
    occrAdd=models.TextField(null=True, blank=True)
    occrDate=models.DateField(null=True, blank=True)
    writngTarget=models.TextField(blank=True)

    def __str__(self):
        return self.name
