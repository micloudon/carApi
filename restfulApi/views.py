from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Car
from .serializer import CarSerializer

def home(request):
    return HttpResponse("Site is Healthy")

def api(request):
    return HttpResponse("Site is Healthy, add all to url to see all JSON objects or add a number to get a specific object")

def car_list(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False)


def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)

    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data)

def car_detail_make(request, make):
    try:
        car = Car.objects.filter(make=make)

    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car, many=True)
        return JsonResponse(serializer.data, safe=False)

def car_detail_model(request, make, model):
    try:
        car = Car.objects.filter(make=make, model=model)

    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car, many=True)
        return JsonResponse(serializer.data, safe=False)

def car_detail_year(request, make, model, year):
    try:
        car = Car.objects.filter(make=make, model=model, year=year)

    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car, many=True)
        return JsonResponse(serializer.data, safe=False)

  
