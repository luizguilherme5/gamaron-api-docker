from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from users.serializers import UserSerializer, GroupSerializer, UserPlayerSerializer
from users.models import UserPlayer
from itens.models import Iten, PlayerInventory
from itens.serializers import ItenSerializer, PlayerInventorySerializer


class ItenViewSet(viewsets.ModelViewSet):

    queryset = Iten.objects.all()
    serializer_class = ItenSerializer

    def get(self, format=None):
        queryset = queryset
        serializer = ItenSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = ItenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class PlayerInvetoryViewSet(viewsets.ModelViewSet):
    queryset = PlayerInventory.objects.all()
    serializer_class = PlayerInventorySerializer
