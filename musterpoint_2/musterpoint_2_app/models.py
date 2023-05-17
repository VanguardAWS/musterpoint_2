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
    # weapon = the weapons associated with that unit
    # wargear_options = the optional wargear associated with that unit

    def __str__(self):
        return self.name

class List(models.Model):
    unit = models.ForeignKey(
        UnitDatasheet,
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner
