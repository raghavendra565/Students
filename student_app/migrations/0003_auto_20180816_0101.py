# Generated by Django 2.1 on 2018-08-16 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_auto_20180816_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='subject',
            field=models.CharField(max_length=20),
        ),
    ]
