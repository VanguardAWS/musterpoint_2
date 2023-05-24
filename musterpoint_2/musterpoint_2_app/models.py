from django.db import models

class UnitDatasheet(models.Model):
    role = models.CharField(max_length=50, null = True, blank = True)
    quantity = models.IntegerField()
    name = models.CharField(max_length=100)
    movement = models.IntegerField()
    weapon_skill = models.IntegerField()
    ballistic_skill = models.IntegerField()
    strength = models.IntegerField()
    toughness = models.IntegerField()
    wounds = models.IntegerField()
    attacks = models.IntegerField()
    leadership = models.IntegerField()
    armor_save = models.IntegerField(null = True, blank = True)
    abilities = models.CharField(max_length=500)
    point_value = models.IntegerField()
    image = models.URLField(null = True, blank = True)
    wargear_options = models.CharField(max_length=500, null = True, blank = True)
    wargear_options_points = models.CharField(max_length=200, null = True, blank = True)
    upgrades = models.CharField(max_length=500, null = True, blank = True)
    upgrades_points = models.CharField(max_length=200, null = True, blank = True)
    # wargear = the weapons associated with that unit

    def __str__(self):
        return self.name
    
class Wargear(models.Model):
    name = models.CharField(max_length=100)
    range = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    armor_penetration = models.IntegerField()
    damage = models.CharField(max_length=200)
    abilities = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class AssociatedWargear(models.Model):
    associated_wargear = models.CharField(max_length=100)
    unit = models.ManyToManyField(UnitDatasheet, related_name='wargear')

    def __str__(self):
        return self.associated_wargear

class List(models.Model):
    unit = models.ForeignKey(
        UnitDatasheet,
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner
