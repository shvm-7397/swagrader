# Generated by Django 2.0.2 on 2018-04-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='score',
            field=models.IntegerField(default=100, null=True),
        ),
    ]