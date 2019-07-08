from django.urls import path, include
from rest_framework.routers import DefaultRouter

from building import views


router = DefaultRouter()
router.register('buildings', views.BuildingViewSet)
router.register('flats', views.FlatViewSet)
router.register('rooms', views.RoomViewSet)
router.register('fixtures', views.FixtureViewSet)

app_name = 'building'

urlpatterns = [
    path('', include(router.urls)),
]
