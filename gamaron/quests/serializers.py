from quests.models import Quest, Journal
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import serializers


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'title', 'description', 'reward_xp',
                  'reward_score', 'reward_iten', 'time_beg',
                  'time_end', 'url', 'creator')


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'quest', 'status',  'player')
