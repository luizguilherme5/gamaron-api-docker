from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

# from gamaron.user_api.views import UserProfileViewSet
from gamaron.users.views import UserViewSet, UserPlayerViewSet, GroupViewSet, PlayerEvolveView
from gamaron.itens.views import ItenViewSet, PlayerInvetoryViewSet
from gamaron.quests.views import QuestViewSet, JournalViewSet
from gamaron.avatar.views import AvatarViewSet


router = DefaultRouter()
# router.register('profile', UserProfileViewSet)
router.register('users', UserViewSet)
router.register('players', UserPlayerViewSet)
router.register('groups', GroupViewSet)
router.register('itens', ItenViewSet)
router.register('inventory', PlayerInvetoryViewSet)
router.register('quests', QuestViewSet)
router.register('journal', JournalViewSet)
router.register('avatar', AvatarViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
