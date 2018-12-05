from quests.models import Quest, Journal
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import serializers
from users.serializers import UserPlayerSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'title', 'description', 'reward_xp',
                  'reward_score', 'reward_iten', 'url', 'creator', 'created_at')


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class JournalSerializer(serializers.ModelSerializer):
    #
    # player = UserPlayerSerializer(many=False, required=True)
    # quest = QuestSerializer(many=False, required=True)

    class Meta:

        model = Journal
        fields = ('id', 'quest', 'status',  'player', 'datetime_beg', 'datetime_end')

        # def create(self, validated_data):
        #
        #     jornal = Jornal.objects.create(**validated_data)
        #
        #     return jornal
