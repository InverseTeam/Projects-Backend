# Generated by Django 3.2.19 on 2023-06-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='experience',
            field=models.IntegerField(blank=True, verbose_name='Опыт'),
        ),
    ]
