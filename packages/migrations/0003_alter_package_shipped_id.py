# Generated by Django 4.1.3 on 2023-04-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_alter_package_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='shipped_id',
            field=models.CharField(default='PJB-00<django.db.models.fields.BigAutoField>', max_length=255),
        ),
    ]
