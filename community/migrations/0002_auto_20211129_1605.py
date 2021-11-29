# Generated by Django 3.0.6 on 2021-11-29 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='likes_user',
            field=models.ManyToManyField(blank=True, related_name='likes_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='community',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cmcomment',
            name='cm_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmcomment', to='community.Community'),
        ),
        migrations.AddField(
            model_name='cmcomment',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmcomment', to=settings.AUTH_USER_MODEL),
        ),
    ]
