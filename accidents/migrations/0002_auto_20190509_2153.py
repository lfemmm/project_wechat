# Generated by Django 2.2.1 on 2019-05-09 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accidents', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='lists',
            new_name='list1',
        ),
        migrations.RenameModel(
            old_name='ranks',
            new_name='rank1',
        ),
        migrations.RenameModel(
            old_name='types',
            new_name='type1',
        ),
    ]
