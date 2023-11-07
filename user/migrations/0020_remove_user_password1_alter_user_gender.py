# Generated by Django 4.2.7 on 2023-11-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0019_alter_user_first_name_alter_user_gender_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="password1",
        ),
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
