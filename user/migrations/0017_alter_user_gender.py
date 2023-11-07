from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0016_merge_20231107_1144"),
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
