# Generated by Django 4.2.8 on 2023-12-31 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauths", "0006_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user", name="username", field=models.CharField(max_length=100),
        ),
    ]
