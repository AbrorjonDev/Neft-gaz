from django.shortcuts import render, get_object_or_404

from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, views, generics, parsers
from rest_framework.response import  Response
# Create your views here.
# from rest_framework.


class AdvertisementViews(views.APIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)

    def get(self, request):
        serializer = self.serializer_class(Advertisement.objects.all(), many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class AdvertisementsDetailView(views.APIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)


    def get(self, request, pk):
        object = get_object_or_404(Advertisement.objects.all(), pk=pk)
        serializer = self.serializer_class(object, many=False)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        object = get_object_or_404(Advertisement.objects.all(), pk=pk)
        serializer = AdvertisementSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        object = get_object_or_404(Advertisement.objects.all(), pk=pk)
        object.delete()
        return Response({'detail':'ok'})

    
# class AdvertisementsDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Advertisement.objects.all()
#     lookup_url_kwarg = 'pk'
#     serializer_class = AdvertisementSerializer
#     permission_classes = (AllowAny,)

class NewsViews(views.APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)

    def get(self, request):
        serializer = self.serializer_class(News.objects.all(), many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class NewsDetailView(views.APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)

    def get(self, request, pk):
        object = get_object_or_404(News.objects.all(), pk=pk)
        serializer = self.serializer_class(object, many=False)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        object = get_object_or_404(News.objects.all(), pk=pk)
        serializer = NewsSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        object = get_object_or_404(News.objects.all(), pk=pk)
        object.delete()
        return Response({'detail':'ok'})


class AccountantsViews(views.APIView):
    queryset = Accountants.objects.all()
    serializer_class = AccountantsSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)

    def get(self, request):
        serializer = self.serializer_class(Accountants.objects.all(), many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class AccountantsDetailView(views.APIView):
    queryset = Accountants.objects.all()
    serializer_class = AccountantsSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)

    def get(self, request, pk):
        object = get_object_or_404(Accountants.objects.all(), pk=pk)
        serializer = self.serializer_class(object, many=False)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        object = get_object_or_404(Accountants.objects.all(), pk=pk)
        serializer = AccountantsSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        object = get_object_or_404(Accountants.objects.all(), pk=pk)
        object.delete()
        return Response({'detail':'ok'})


class TendersViews(views.APIView):
    queryset = Tenders.objects.all()
    serializer_class = TendersSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)

    def get(self, request):
        serializer = self.serializer_class(Tenders.objects.all(), many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class TendersDetailView(views.APIView):
    queryset = Tenders.objects.all()
    serializer_class = TendersSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)

    def get(self, request, pk):
        object = get_object_or_404(Tenders.objects.all(), pk=pk)
        serializer = self.serializer_class(object, many=False)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        object = get_object_or_404(Tenders.objects.all(), pk=pk)
        serializer = TendersSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        object = get_object_or_404(Tenders.objects.all(), pk=pk)
        object.delete()
        return Response({'detail':'ok'})

class NounsViews(views.APIView):
    queryset = Nouns.objects.all()
    serializer_class =NounsSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)

    def get(self, request):
        serializer = self.serializer_class(Nouns.objects.all(), many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class NounsDetailView(views.APIView):
    queryset = Nouns.objects.all()
    serializer_class = NounsSerializer
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)

    def get(self, request, pk):
        object = get_object_or_404(Nouns.objects.all(), pk=pk)
        serializer = self.serializer_class(object, many=False)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        object = get_object_or_404(Nouns.objects.all(), pk=pk)
        serializer = NounsSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        object = get_object_or_404(Nouns.objects.all(), pk=pk)
        object.delete()
        return Response({'detail':'ok'})