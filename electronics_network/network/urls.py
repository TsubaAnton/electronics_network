from .apps import NetworkConfig
from django.urls import path
from .views import (NetworkLinkListAPIView, NetworkLinkCreateAPIView,
                    NetworkLinkRetrieveAPIView, NetworkLinkUpdateAPIView, NetworkLinkDestroyAPIView)

app_name = NetworkConfig.name

urlpatterns = [
    path('networklink/', NetworkLinkListAPIView.as_view(), name='networklink_list'),
    path('networklink/create/', NetworkLinkCreateAPIView.as_view(), name='networklink_create'),
    path('networklink/<int:pk>/', NetworkLinkRetrieveAPIView.as_view(), name='networklink_retrieve'),
    path('networklink/update/<int:pk>/', NetworkLinkUpdateAPIView.as_view(), name='networklink_update'),
    path('networklink/destroy/<int:pk>/', NetworkLinkDestroyAPIView.as_view(), name='networklink_destroy'),
]
