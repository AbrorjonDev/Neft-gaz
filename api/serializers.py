from rest_framework import serializers
from .models import *

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class AccountantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountants
        fields = "__all__"


class TendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenders
        fields = "__all__"


class NounsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nouns
        fields = "__all__"

