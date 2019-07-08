# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import viewsets, mixins, status
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Building, Flat, Room, Fixture

from building import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(name__isnull=False)

        return queryset.filter(
            user=self.request.user
        ).order_by('-name').distinct()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """Update a object"""
        serializer.save(user=self.request.user)


class BuildingViewSet(BaseRecipeAttrViewSet):
    """Manage buildings in the database"""
    queryset = Building.objects.all()
    serializer_class = serializers.BuildingSerializer

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        buildings = self.request.query_params.get('search')
        queryset = self.queryset
        if buildings:
            queryset = queryset.filter(name__contains=buildings)

        return queryset.filter(user=self.request.user)


class FlatViewSet(BaseRecipeAttrViewSet):
    """Manage flats in the database"""
    queryset = Flat.objects.all()
    serializer_class = serializers.FlatSerializer

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        flats = self.request.query_params.get('search')
        queryset = self.queryset
        if flats:
            queryset = queryset.filter(name__contains=flats)

        return queryset.filter(user=self.request.user)


class RoomViewSet(BaseRecipeAttrViewSet):
    """Manage rooms in the database"""
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        rooms = self.request.query_params.get('search')
        queryset = self.queryset
        if rooms:
            queryset = queryset.filter(name__contains=rooms)

        return queryset.filter(user=self.request.user)


class FixtureViewSet(BaseRecipeAttrViewSet):
    """Manage fixtures in the database"""
    queryset = Fixture.objects.all()
    serializer_class = serializers.FixtureSerializer

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        fixtures = self.request.query_params.get('search')
        queryset = self.queryset
        if fixtures:
            queryset = queryset.filter(name__contains=fixtures)

        return queryset.filter(user=self.request.user)
