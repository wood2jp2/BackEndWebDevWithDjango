# Generated by Django 2.2 on 2019-04-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videorequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videoTitle',
            field=models.CharField(max_length=40),
        ),
    ]
