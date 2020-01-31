# Generated by Django 3.0.2 on 2020-01-31 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='winners_page_layout_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='winners_page_layout_type', to='pool.PageLayoutType'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='picks_page_layout_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picks_page_layout_type', to='pool.PageLayoutType'),
        ),
    ]