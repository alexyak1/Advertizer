from rest_framework import serializers
from rest_advert.models import Ad

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'subject', 'body', 'price', 'email']
