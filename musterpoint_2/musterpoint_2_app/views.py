from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import UnitDatasheet, Wargear, List
from .serializers import UnitDatasheetSerializer, WargearSerializer, ListSerializer


def index(request):
    return HttpResponse('ok')

class UnitDatasheetViewSet(viewsets.ModelViewSet):
    queryset = UnitDatasheet.objects.all()
    serializer_class = UnitDatasheetSerializer

class WargearViewSet(viewsets.ModelViewSet):
    queryset = Wargear.objects.all()
    serializer_class = WargearSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer