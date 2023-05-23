# Generated by Django 4.2.1 on 2023-05-22 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitDatasheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('movement', models.IntegerField()),
                ('weapon_skill', models.IntegerField()),
                ('ballistic_skill', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('toughness', models.IntegerField()),
                ('wounds', models.IntegerField()),
                ('attacks', models.IntegerField()),
                ('leadership', models.IntegerField()),
                ('armor_save', models.IntegerField(blank=True, null=True)),
                ('abilities', models.CharField(max_length=500)),
                ('point_value', models.IntegerField()),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musterpoint_2_app.unitdatasheet')),
            ],
        ),
    ]