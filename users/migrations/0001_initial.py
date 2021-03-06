# Generated by Django 2.2.1 on 2019-05-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('sex', models.CharField(blank=True, max_length=5, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('company_code', models.CharField(blank=True, max_length=20, null=True)),
                ('company_name', models.CharField(blank=True, max_length=20, null=True)),
                ('position', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
