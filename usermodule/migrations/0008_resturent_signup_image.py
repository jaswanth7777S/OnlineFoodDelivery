# Generated by Django 5.0.1 on 2024-02-19 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0007_add_food_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturent_signup',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]