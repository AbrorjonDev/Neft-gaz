from django.shortcuts import render
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
# Create your views here.
# from rest_framework.


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (AllowAny,)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)



class AccountantsViewSet(viewsets.ModelViewSet):
    queryset = Accountants.objects.all()
    serializer_class = AccountantsSerializer
    permission_classes = (AllowAny,)


class TendersViewSet(viewsets.ModelViewSet):
    queryset = Tenders.objects.all()
    serializer_class = TendersSerializer
    permission_classes = (AllowAny,)



class NounsViewSet(viewsets.ModelViewSet):
    queryset = Nouns.objects.all()
    serializer_class =NounsSerializer
    permission_classes = (AllowAny,)