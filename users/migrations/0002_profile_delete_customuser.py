# Generated by Django 5.0.6 on 2024-06-26 07:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=24, null=True)),
                ('last_name', models.CharField(blank=True, max_length=24, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('last_active', models.CharField(blank=True, max_length=512, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
