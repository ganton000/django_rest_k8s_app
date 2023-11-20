# Generated by Django 4.2.7 on 2023-11-20 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("pet_name", models.CharField(max_length=20)),
                ("pet_breed", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("owner_email", models.EmailField(max_length=254, unique=True)),
                ("owner_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name="Users",
        ),
    ]