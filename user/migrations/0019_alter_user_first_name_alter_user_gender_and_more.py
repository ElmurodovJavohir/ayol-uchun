# Generated by Django 4.2.7 on 2023-11-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0018_user_password1_alter_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
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
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
