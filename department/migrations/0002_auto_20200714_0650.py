# Generated by Django 3.0.8 on 2020-07-14 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ('created_at',)},
        ),
    ]