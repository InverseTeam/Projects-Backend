# Generated by Django 3.2.18 on 2023-09-24 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_outcoming_applications_project_outgoing_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomingapplication',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='incoming_applications_project', to='projects.project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]
