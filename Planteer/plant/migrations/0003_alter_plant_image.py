# Generated by Django 5.1.3 on 2024-11-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0002_category_alter_plant_options_plant_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='plants/'),
        ),
    ]
