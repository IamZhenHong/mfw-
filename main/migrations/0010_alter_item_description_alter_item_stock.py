# Generated by Django 4.2.5 on 2024-02-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_remove_item_image_itemimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="stock",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
