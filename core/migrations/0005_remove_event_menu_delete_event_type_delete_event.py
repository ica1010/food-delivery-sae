# Generated by Django 5.0.3 on 2024-04-07 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_commande_menu_date_commande_plat_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Event_type',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
