# Generated by Django 5.1.1 on 2024-09-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_customuser_c1_connected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]