import json

from django.core.management.base import BaseCommand

from ...models import UnitDatasheet, Wargear, AssociatedWargear

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        # Clear existing Datasheets and Wargear
        UnitDatasheet.objects.all().delete()
        Wargear.objects.all().delete()

        # Open Imperial Knights Units JSON and load to list of dictionaries
        with open('imperial_knights_units.json') as p:
            imperial_knights_units_list = json.loads(p.read())

        # Open Imperial Knights Wargear JSON and load to list of dictionaries
        with open('imperial_knights_wargear.json') as p:
            imperial_knights_wargear_list = json.loads(p.read())
        
        # Loop through units to add to DB
        for imperial_knight_unit in imperial_knights_units_list['imperial_knight_unit']:

            # Add units to DB
            imperial_knight_unit_obj = UnitDatasheet.objects.create(
                role=imperial_knight_unit['role'],
                quantity=imperial_knight_unit['quantity'],
                name=imperial_knight_unit['name'],
                movement=imperial_knight_unit['movement'],
                weapon_skill=imperial_knight_unit['weapon_skill'],
                ballistic_skill=imperial_knight_unit['ballistic_skill'],
                strength=imperial_knight_unit['strength'],
                toughness=imperial_knight_unit['toughness'],
                wounds=imperial_knight_unit['wounds'],
                attacks=imperial_knight_unit['attacks'],
                leadership=imperial_knight_unit['leadership'],
                armor_save=imperial_knight_unit['armor_save'],
                abilities=imperial_knight_unit['abilities'],
                point_value=imperial_knight_unit['point_value'],
                image=imperial_knight_unit['image'],
                wargear_options=imperial_knight_unit['wargear_options'],
                wargear_options_points=imperial_knight_unit['wargear_options_points'],
                upgrades=imperial_knight_unit['upgrades'],
                upgrades_points=imperial_knight_unit['upgrades_points']

            )

            for associated_wargear in imperial_knight_unit['wargear']:
                associated_wargear_obj, created = AssociatedWargear.objects.get_or_create(associated_wargear=associated_wargear)
                associated_wargear_obj.unit.add(imperial_knight_unit_obj)

        # Loop through units to add to DB
        for imperial_knight_wargear in imperial_knights_wargear_list['wargear']:

            # Add wargear to DB
            imperial_knight_wargear_obj = Wargear.objects.create(
                name=imperial_knight_wargear['name'],
                range=imperial_knight_wargear['range'],
                type=imperial_knight_wargear['type'],
                strength=imperial_knight_wargear['strength'],
                armor_penetration=imperial_knight_wargear['armor_penetration'],
                damage=imperial_knight_wargear['damage'],
                abilities=imperial_knight_wargear['abilities']
            )

        

        
