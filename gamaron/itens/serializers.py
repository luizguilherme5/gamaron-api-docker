from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password
from itens.models import Iten, PlayerInventory
from users.serializers import UserPlayerSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import serializers

@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ItenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iten
        fields = ('id', 'name', 'description')


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class PlayerInventorySerializer(serializers.ModelSerializer):
    # user = UserPlayerSerializer(many=False, required=True)
    # itens = ItenSerializer(many=True, required=False)

    class Meta:
        model = PlayerInventory
        fields = ('id', 'player', 'itens')

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        # user_data = validated_data.pop('player')

        inventory = PlayerInventory.objects.create(**validated_data)
        # inventory.player = Users.objects.get(id=user_data)

        for iten in itens_data:
            inventory.itens.add(iten)

        return inventory
