# Generated by Django 3.2.9 on 2021-12-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='hidden',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hidden',
            field=models.BooleanField(default=True),
        ),
    ]
