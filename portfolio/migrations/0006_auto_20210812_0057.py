# Generated by Django 3.0.6 on 2021-08-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_business_field_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='price',
            field=models.IntegerField(),
        ),
    ]
