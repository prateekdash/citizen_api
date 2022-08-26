from encodings import search_function
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .serializers import usersserializers
from .models import users
from api import serializers
from .mypaginations import MyLimitOffsetPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/users-GET/',
        'Detail View': '/users-detail/<int:id>/',
        'Create': '/users-create/',
        'Update': '/users-update/<int:id>/',
        'Delete': '/users-detail/<int:id>/',
    }

    return Response(api_urls);

class userslist(ListAPIView):
    queryset= users.objects.all()
    serializer_class = usersserializers
    pagination_class = MyLimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields =  ('id','first_name','last')
    search_fields = ('id','first_name','last_name')

@api_view(['GET'])
def ShowAll(request):
    usersdata = users.objects.all()
 #   pagination_class = MyLimitOffsetPagination
    serializer = usersserializers(usersdata, many=True)
  #  filter_backends = (DjangoFilterBackend, SearchFilter)
   # filter_fields =  ('id','first_name','last')
    #search_fields = ('id','first_name','last_name')
    return Response(serializer.data)

@api_view(['GET'])
def viewusers(request, pk):
    usersdata = users.objects.filter(id = pk)
    serializer = usersserializers(usersdata, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createusers(request):
    serializer = usersserializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateusers(request, pk):
    user = users.objects.get(id = pk)
    serializer = usersserializers(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteusers(request, pk):
    user = users.objects.get(id = pk)
    user.delete()

    return Response('Items deleted successfully!')



