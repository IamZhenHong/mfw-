# Generated by Django 4.2.5 on 2024-02-04 03:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0019_user_alter_order_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
