# Generated by Django 3.0.6 on 2020-06-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='course_code',
            field=models.CharField(max_length=6),
        ),
    ]