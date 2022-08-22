from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import citizensserilizer
from .models import citizens
from api import serializers

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/citizens-GET/',
        'Detail View': '/product-detail/<int:id>/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>/',
        'Delete': '/product-detail/<int:id>/',
    }

    return Response(api_urls);

@api_view(['GET'])
def ShowAll(request):
    citizens = citizens.objects.all()
    serializer = citizensserilizer(citizens, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Viewcitizens(request, pk):
    citizen = citizens.objects.all(id = pk)
    serializer = citizensserilizer(citizens, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Createcitizens(request):
    serializer = citizensserilizer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Updatecitizens(request, pk):
    citizen = citizens.objects.get(id = pk)
    serializer = citizensserilizer(instance=citizen, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deletecitizens(request, pk):
    citizen = citizens.objects.get(id = pk)
    citizen.delete()

    return Response('Items deleted successfully!')



