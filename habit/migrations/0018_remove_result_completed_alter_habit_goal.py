# Generated by Django 4.0.3 on 2022-03-31 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0017_alter_habit_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='completed',
        ),
        migrations.AlterField(
            model_name='habit',
            name='goal',
            field=models.IntegerField(),
        ),
    ]
