# Generated by Django 4.2.1 on 2023-06-02 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='number',
            field=models.PositiveIntegerField(default=0, verbose_name='Number of data to generate'),
            preserve_default=False,
        ),
    ]
