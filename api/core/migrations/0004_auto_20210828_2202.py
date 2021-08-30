# Generated by Django 3.1.3 on 2021-08-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('BUS', 'Business'), ('REG', 'Regular'), ('ADM', 'Admin')], default='REG', max_length=3),
        ),
    ]
