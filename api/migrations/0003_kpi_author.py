# Generated by Django 5.1.1 on 2024-09-17 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_organization_description_usertype_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpi',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
