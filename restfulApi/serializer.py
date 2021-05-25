from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.Serializer):
    make = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    year = serializers.IntegerField()
    fuelType = serializers.CharField(max_length=299)
    horsePower = serializers.IntegerField()
    cylinders = serializers.IntegerField()
    driveTrain = serializers.CharField(max_length=299)
    numDoors = serializers.IntegerField()
    size = serializers.CharField(max_length=299)
    style = serializers.CharField(max_length=299)
    highwayMpg = serializers.IntegerField()
    cityMpg = serializers.IntegerField()
    msrp = serializers.IntegerField()

    def create(self, validated_data):
        return Car.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.make = validated_data.get('make', instance.make)
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        instance.fuelType = validated_data.get('fuelType', instance.fuelType)
        instance.horsePower = validated_data.get('horsePower', instance.horsePower)
        instance.cylinders = validated_data.get('cylinders', instance.cylinders)
        instance.driveTrain = validated_data.get('driveTrain', instance.driveTrain)
        instance.numDoors = validated_data.get('numDoors', instance.numDoors)
        instance.size = validated_data.get('size', instance.size)
        instance.style = validated_data.get('style', instance.style)
        instance.highwayMpg = validated_data.get('highwayMpg', instance.highwayMpg)
        instance.cityMpg = validated_data.get('cityMpg', instance.cityMpg)
        instance.msrp = validated_data.get('msrp', instance.msrp)

        instance.save()
        
        return instance


