# Generated by Django 4.2.9 on 2024-02-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_studentdata_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='skills',
            field=models.CharField(max_length=200),
        ),
    ]
