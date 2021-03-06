# Generated by Django 4.0.4 on 2022-05-12 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nitrogen', models.PositiveIntegerField(null=True)),
                ('phosphorus', models.PositiveIntegerField(null=True)),
                ('potassium', models.PositiveIntegerField(null=True)),
                ('temperature', models.PositiveIntegerField(null=True)),
                ('humidity', models.PositiveIntegerField(null=True)),
                ('ph', models.PositiveIntegerField(null=True)),
                ('rainfall', models.PositiveIntegerField(null=True)),
                ('predicted_crop', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
