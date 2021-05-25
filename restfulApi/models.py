from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    fuelType = models.CharField(max_length=299)
    horsePower = models.IntegerField()
    cylinders = models.IntegerField()
    driveTrain = models.CharField(max_length=299)
    numDoors = models.IntegerField()
    size = models.CharField(max_length=299)
    style = models.CharField(max_length=299)
    highwayMpg = models.IntegerField()
    cityMpg = models.IntegerField()
    msrp = models.IntegerField()



