# Generated by Django 4.2.1 on 2023-06-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_record_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
