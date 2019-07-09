from rest_framework import serializers

from core.models import Building, Flat, Room, Fixture
from django.db import models


class BuildingSerializer(serializers.ModelSerializer):
    """Serializer for building objects"""
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        obj.total_price = 0
        obj.flat_id = []
        obj.room_id = []
        obj.room = None

        obj.flat = Flat.objects.filter(building_id=obj.id)
        for item in obj.flat:
            obj.flat_id.append(item.id)

        if obj.flat_id:
            obj.room = Room.objects.filter(flat_id__in=obj.flat_id)

        if obj.room:
            for item in obj.room:
                obj.room_id.append(item.id)

            if obj.room_id:
                obj.total_price = Fixture.objects.filter(
                    room_id__in=obj.room_id
                ).aggregate(total=models.Sum('price_value'))

        return obj.total_price

    class Meta:
        model = Building
        fields = ('id', 'name', 'total_price')
        read_only_fields = ('id',)


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(
            UserFilteredPrimaryKeyRelatedField, self
        ).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(user=request.user)


class FlatSerializer(serializers.ModelSerializer):
    """Serializer for flat objects"""
    building_name = serializers.ReadOnlyField(source='building_id.name')
    building_id = UserFilteredPrimaryKeyRelatedField(queryset=Building.objects)

    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        obj.total_price = 0
        obj.room_id = []
        obj.room = Room.objects.filter(flat_id=obj.id)

        for item in obj.room:
            obj.room_id.append(item.id)

        if obj.room_id:
            obj.total_price = Fixture.objects.filter(
                room_id__in=obj.room_id
            ).aggregate(total=models.Sum('price_value'))

        return obj.total_price

    class Meta:
        model = Flat
        fields = (
            'id', 'name', 'building_id', 'building_name',
            'total_price',
        )
        read_only_fields = ('id',)


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for flat objects"""
    flat_name = serializers.ReadOnlyField(source='flat_id.name')
    flat_id = UserFilteredPrimaryKeyRelatedField(queryset=Flat.objects)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        obj.total_price = Fixture.objects.filter(
            room_id=obj.id
        ).aggregate(total=models.Sum('price_value'))

        return obj.total_price

    class Meta:
        model = Room
        fields = (
            'id', 'name', 'flat_id',
            'flat_name', 'total_price',
        )
        read_only_fields = ('id', 'flat_name',)


class FixtureSerializer(serializers.ModelSerializer):
    """Serializer for flat objects"""
    room_name = serializers.ReadOnlyField(source='room_id.name')
    room_id = UserFilteredPrimaryKeyRelatedField(queryset=Room.objects)

    class Meta:
        model = Fixture
        fields = (
            'id', 'name', 'room_id',
            'price_value', 'room_name',
        )
        read_only_fields = ('id', 'room_name',)
