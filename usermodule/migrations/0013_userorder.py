# Generated by Django 5.0.1 on 2024-03-09 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0012_alter_order_food_alter_order_res'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=25)),
                ('ordered', models.CharField(default=False)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermodule.add_food')),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermodule.resturent_signup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermodule.user_signup')),
            ],
        ),
    ]
