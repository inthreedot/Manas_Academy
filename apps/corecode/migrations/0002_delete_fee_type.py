# Generated by Django 4.1.7 on 2023-04-10 09:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0002_alter_invoiceitem_description"),
        ("corecode", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="fee_type",
        ),
    ]
