# Generated by Django 5.1.4 on 2024-12-06 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("func", "0004_alter_cartentry_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartentry",
            name="item",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="func.item"
            ),
        ),
    ]
