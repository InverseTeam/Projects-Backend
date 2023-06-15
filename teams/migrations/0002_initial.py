# Generated by Django 3.2.19 on 2023-06-15 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='invites',
            field=models.ManyToManyField(related_name='teams_invites', to=settings.AUTH_USER_MODEL, verbose_name='Приглашения'),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='teams_member', to=settings.AUTH_USER_MODEL, verbose_name='Участники'),
        ),
        migrations.AddField(
            model_name='team',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teams_mentor', to=settings.AUTH_USER_MODEL, verbose_name='Ментор'),
        ),
        migrations.AddField(
            model_name='team',
            name='teamlead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teams_teamlead', to=settings.AUTH_USER_MODEL, verbose_name='Тимлид'),
        ),
    ]
