# Generated by Django 5.1.7 on 2025-03-18 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_tour_guide',
            field=models.BooleanField(default=False),
        ),
    ]
