from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

# from gamaron.user_api.views import UserProfileViewSet
from gamaron.users.views import UserViewSet
from gamaron.itens.views import ItenViewSet
from gamaron.quests.views import QuestViewSet

router = DefaultRouter()
# router.register('profile', UserProfileViewSet)
router.register('users', UserViewSet)
router.register('itens', ItenViewSet)
router.register('quests', QuestViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
