from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from users.serializers import UserSerializer, GroupSerializer, UserPlayerSerializer
from users.models import UserPlayer


class UserViewSet(viewsets.ModelViewSet):

    queryset = UserPlayer.objects.all()
    serializer_class = UserPlayerSerializer

    def get(self, format=None):
        players = UserPlayer.objects.all()
        serializer = UserPlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = UserPlayerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
