# Generated by Django 4.1.2 on 2022-11-04 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0002_blog_rename_secciones_seccion"),
    ]

    operations = [
        migrations.RenameField(
            model_name="autor",
            old_name="profecion",
            new_name="profesion",
        ),
    ]
