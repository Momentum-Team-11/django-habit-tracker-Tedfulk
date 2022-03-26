# Generated by Django 4.0.3 on 2022-03-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0010_habit_user_alter_result_habit_record'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='result',
            name='one_record_per_day',
        ),
        migrations.AddConstraint(
            model_name='result',
            constraint=models.UniqueConstraint(fields=('habit_record', 'update_date'), name='one_record_per_day'),
        ),
    ]