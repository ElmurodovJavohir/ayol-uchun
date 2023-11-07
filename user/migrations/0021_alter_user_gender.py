# Generated by Django 4.1 on 2023-11-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0020_alter_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("Erkak", "Male"), ("Ayol", "Female")],
                default="Ayol",
                max_length=255,
            ),
        ),
    ]
