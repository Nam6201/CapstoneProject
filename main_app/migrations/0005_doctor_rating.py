# Generated by Django 2.2.5 on 2019-12-08 19:28

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20191209_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
