# Generated by Django 4.1 on 2022-08-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_scope"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="scope",
            field=models.FileField(blank=True, upload_to="uploads/"),
        ),
    ]
