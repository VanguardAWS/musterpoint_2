from rest_framework import serializers
from .models import UnitDatasheet, Wargear, List, AssociatedWargear

class AssociatedWargearSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('associated_wargear')
        model = AssociatedWargear

class WargearSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Wargear


class UnitDatasheetSerializer(serializers.ModelSerializer):
    wargear = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        fields = (
            'role',
            'quantity', 
            'name', 
            'movement', 
            'weapon_skill', 
            'ballistic_skill', 
            'strength', 
            'toughness', 
            'wounds', 
            'attacks', 
            'leadership', 
            'armor_save', 
            'abilities', 
            'point_value', 
            'image', 
            'wargear_options',
            'wargear_options_points',
            'upgrades',
            'upgrades_points',
            'wargear' 
        )
        model = UnitDatasheet

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = List