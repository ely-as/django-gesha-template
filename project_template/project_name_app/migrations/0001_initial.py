# Generated by Django 4.2

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enquiry",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="Email address"),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=17, verbose_name="Phone number"),
                ),
                ("description", models.TextField(verbose_name="Description")),
            ],
            options={
                "verbose_name_plural": "enquiries",
                "ordering": ["-created"],
                "get_latest_by": "created",
            },
        ),
    ]
