from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthViewSet, PlayerViewSet

router = DefaultRouter()

router.register('user', PlayerViewSet)
router.register('auth', AuthViewSet, 'auth')


urlpatterns = [
    path('', include(router.urls))
]
