# Generated by Django 4.1.7 on 2023-04-09 20:56

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "current_status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=10,
                    ),
                ),
                ("firstname", models.CharField(max_length=200)),
                ("surname", models.CharField(max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("Other", "Other"),
                        ],
                        default="male",
                        max_length=10,
                    ),
                ),
                ("date_of_birth", models.DateField(default=django.utils.timezone.now)),
                (
                    "date_of_Joining",
                    models.DateField(default=django.utils.timezone.now),
                ),
                (
                    "mobile_number",
                    models.CharField(
                        blank=True,
                        max_length=13,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Entered mobile number isn't in a right format!",
                                regex="^[0-9]{10,15}$",
                            )
                        ],
                    ),
                ),
                ("address", models.TextField(blank=True)),
                ("others", models.TextField(blank=True)),
            ],
        ),
    ]