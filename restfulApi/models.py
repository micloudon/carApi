from django.db import models

class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    fuelType = models.CharField(max_length=299)
    horsePower = models.IntegerField(null=True, blank=True)
    cylinders = models.IntegerField(null=True, blank=True)
    driveTrain = models.CharField(max_length=299)
    numDoors = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=299)
    style = models.CharField(max_length=299)
    highwayMpg = models.IntegerField()
    cityMpg = models.IntegerField()
    msrp = models.IntegerField()



