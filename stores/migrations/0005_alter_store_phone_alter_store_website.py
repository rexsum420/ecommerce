# Generated by Django 5.0.6 on 2024-07-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_alter_store_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='store',
            name='website',
            field=models.URLField(blank=True, default=''),
        ),
    ]
