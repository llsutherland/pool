# Generated by Django 3.0.2 on 2020-02-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0002_standings'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='site_width',
            field=models.CharField(default='wide', max_length=10),
        ),
    ]
