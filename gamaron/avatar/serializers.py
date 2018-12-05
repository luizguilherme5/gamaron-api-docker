from avatar.models import Avatar
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import serializers

@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('id','name', 'image')
