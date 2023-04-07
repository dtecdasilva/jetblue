# Generated by Django 4.1.3 on 2023-04-06 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('shipped_from', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('shipped_id', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]