# Generated by Django 3.2.19 on 2023-06-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='experience',
            field=models.IntegerField(blank=True, default=0, verbose_name='Опыт'),
        ),
    ]
