# Generated by Django 5.1.1 on 2024-09-18 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_organization_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.organization'),
        ),
    ]