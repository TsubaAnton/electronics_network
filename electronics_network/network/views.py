from rest_framework import generics
from .serializers import NetworkLinkSerializer, NetworkLinkUpdateSerializer
from .models import NetworkLink
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActiveUser


class NetworkLinkListAPIView(generics.ListAPIView):
    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [IsAuthenticated, IsActiveUser]


class NetworkLinkCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
    permission_classes = [IsAuthenticated, IsActiveUser]


class NetworkLinkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
    permission_classes = [IsAuthenticated, IsActiveUser]


class NetworkLinkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NetworkLinkUpdateSerializer
    queryset = NetworkLink.objects.all()
    permission_classes = [IsAuthenticated, IsActiveUser]


class NetworkLinkDestroyAPIView(generics.DestroyAPIView):
    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
    permission_classes = [IsAuthenticated, IsActiveUser]
