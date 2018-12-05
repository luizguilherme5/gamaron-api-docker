from avatar.models import Avatar
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.views import APIView
from avatar.serializers import AvatarSerializer

class AvatarViewSet(viewsets.ModelViewSet):

    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
