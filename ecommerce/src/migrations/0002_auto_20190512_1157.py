# Generated by Django 2.2.1 on 2019-05-12 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oils',
            new_name='Nut',
        ),
        migrations.RenameModel(
            old_name='Nuts',
            new_name='Oil',
        ),
        migrations.RenameModel(
            old_name='Pasta_Noodles',
            new_name='Pasta_Noodle',
        ),
    ]
