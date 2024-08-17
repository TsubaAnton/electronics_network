from rest_framework import serializers
from .models import NetworkLink


class NetworkLinkUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetworkLink
        exclude = ['debt']


class NetworkLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetworkLink
        fields = '__all__'
