from rest_framework import viewsets
from quests.serializers import QuestSerializer, JournalSerializer
from quests.models import Quest, Journal


class QuestViewSet(viewsets.ModelViewSet):

    queryset = Quest.objects.all()
    serializer_class = QuestSerializer

    def get(self, format=None):
        queryset = queryset
        serializer = QuestSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = QuestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class JournalViewSet(viewsets.ModelViewSet):

    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def get(self, format=None):
        queryset = queryset
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)