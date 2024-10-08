# Generated by Django 5.1.1 on 2024-09-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_kpi_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='code',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tg_code',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tg_username',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
