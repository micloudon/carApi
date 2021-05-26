from rest_framework import fields, serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
   class Meta:
       model = Car
       fields = ['id', 'make', 'model', 'year', 'fuelType', 'horsePower',
    'cylinders', 'driveTrain', 'numDoors', 'size', 'style', 'highwayMpg', 'cityMpg', 'msrp']


