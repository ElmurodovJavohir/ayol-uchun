# Generated by Django 4.1 on 2023-11-07 17:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_rename_in_process_video_in_process_watching"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="certificate_identifier",
            field=models.CharField(
                auto_created=True,
                default=uuid.UUID("93e64625-79ed-447f-929a-6e92211351dc"),
                editable=False,
                max_length=77,
                unique=True,
            ),
        ),
    ]