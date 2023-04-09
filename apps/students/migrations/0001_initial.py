# Generated by Django 4.1.7 on 2023-04-09 20:56

import apps.students.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("corecode", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentBulkUpload",
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
                ("date_uploaded", models.DateTimeField(auto_now=True)),
                ("csv_file", models.FileField(upload_to="students/bulkupload/")),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                (
                    "registration_number",
                    models.CharField(
                        blank=True,
                        default=apps.students.models.increment_reg_number,
                        max_length=500,
                        null=True,
                    ),
                ),
                ("firstname", models.CharField(max_length=200)),
                ("surname", models.CharField(max_length=200)),
                ("fathers_name", models.CharField(blank=True, max_length=200)),
                ("mothers_name", models.CharField(blank=True, max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        default="male",
                        max_length=10,
                    ),
                ),
                ("date_of_birth", models.DateField(default=django.utils.timezone.now)),
                (
                    "date_of_admission",
                    models.DateField(default=django.utils.timezone.now),
                ),
                (
                    "parent_mobile_number",
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
                (
                    "Students_Category",
                    models.CharField(
                        choices=[
                            ("General", "General"),
                            ("SC", "SC"),
                            ("ST", "ST"),
                            ("OBC", "OBC"),
                            ("MOBC", "MOBC"),
                            ("Others", "Others"),
                        ],
                        default="General",
                        max_length=15,
                    ),
                ),
                (
                    "educational_block",
                    models.CharField(default="Bhabanipur Block", max_length=200),
                ),
                ("cluster_name", models.CharField(blank=True, max_length=200)),
                ("address", models.TextField(blank=True)),
                ("district", models.CharField(default="Barpeta", max_length=200)),
                ("state", models.CharField(default="Assam", max_length=200)),
                ("country", models.CharField(default="India", max_length=200)),
                (
                    "pin",
                    models.CharField(
                        default=None,
                        max_length=6,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Entered Pin number isn't in a right format!",
                                regex="^[0-9]{5,7}$",
                            )
                        ],
                    ),
                ),
                (
                    "aadhaar_number",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="please entere a correct Aadhar number !",
                                regex="^[0-9]{11,13}$",
                            )
                        ],
                    ),
                ),
                ("name_of_the_bank", models.CharField(blank=True, max_length=200)),
                (
                    "account_no",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Entered bank account number isn't in a right format!",
                                regex="^[0-9]{10,20}$",
                            )
                        ],
                    ),
                ),
                ("branch_name", models.CharField(blank=True, max_length=200)),
                ("ifsc_code", models.CharField(blank=True, max_length=10)),
                ("others", models.TextField(blank=True)),
                (
                    "student_photo",
                    models.ImageField(blank=True, upload_to="students/student_photos/"),
                ),
                (
                    "birth_certificate",
                    models.FileField(
                        blank=True, null=True, upload_to="students/birth_certificate/"
                    ),
                ),
                (
                    "current_class",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="corecode.studentclass",
                    ),
                ),
            ],
            options={
                "ordering": ["firstname", "surname"],
            },
        ),
    ]