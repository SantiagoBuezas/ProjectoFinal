# Generated by Django 4.1.2 on 2022-11-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("tema", models.CharField(max_length=50)),
                ("fecha", models.DateField(null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name="secciones",
            new_name="Seccion",
        ),
    ]
