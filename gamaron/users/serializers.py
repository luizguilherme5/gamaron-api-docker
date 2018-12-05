from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password
from users.models import UserPlayer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import serializers

@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'url')


@permission_classes((permissions.AllowAny,))
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups',  'password')
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            password=make_password(validated_data['password'])
        )
        user.save()

        groups_data = validated_data.pop('groups')
        for group in groups_data:
                # usergroup = Group.objects.get(id=group['id'])
                user.groups.add(group)
        user.save()
        return user



@permission_classes((permissions.AllowAny,))
class UserPlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = UserPlayer
        fields = ('id', 'user', 'xp')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of userplayer
        :return: returns a successfully created student userplayer
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        player, created = UserPlayer.objects.update_or_create(user=user,
                            xp=validated_data.pop('xp'))
        player.save()
        return player
