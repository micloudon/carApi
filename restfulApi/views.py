from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Car
from .serializer import CarSerializer
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Site is functional")

def api(request):
    return HttpResponse("add all to url to see all JSON objects or add a number to get a specific object")

@csrf_exempt
def car_list(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)

    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarSerializer(car, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        car.delete()
        return HttpResponse(status=204)
