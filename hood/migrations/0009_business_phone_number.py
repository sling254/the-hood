# Generated by Django 3.2.9 on 2022-01-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]