# Generated by Django 4.0.3 on 2022-03-28 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0, verbose_name='likes'),
        ),
    ]
