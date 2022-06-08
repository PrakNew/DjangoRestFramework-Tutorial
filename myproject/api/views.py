from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import ItemSerializer
from base.models import Item

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer  = ItemSerializer(items,many=True)#many = True means we are gonna serialize multiple items whereas False means for one item only
    print('-'*25,serializer.data, type(serializer.data))
    return Response(serializer.data)#list of OrderedDict is returned
# Create your views here.

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)