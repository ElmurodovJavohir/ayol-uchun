# Generated by Django 4.1 on 2023-11-07 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_article_slug"),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={"verbose_name": "Course", "verbose_name_plural": "Courses"},
        ),
        migrations.AddField(
            model_name="course",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="course",
            name="description",
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="course",
            name="image",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.blogimages",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="course",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
