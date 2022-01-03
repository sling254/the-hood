# Generated by Django 3.2.9 on 2022-01-03 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0002_userprofile_neighborhood_business_neighborhood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='auth.user', verbose_name='user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.DeleteModel(
            name='NeighborHood',
        ),
    ]