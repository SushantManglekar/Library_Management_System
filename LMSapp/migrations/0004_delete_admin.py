# Generated by Django 4.1 on 2022-09-12 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("LMSapp", "0003_rename_firstname_admin_username_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Admin",),
    ]
