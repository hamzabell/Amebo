# Generated by Django 3.1.3 on 2021-08-30 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_auto_20210830_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='business',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.business'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.product'),
        ),
    ]
