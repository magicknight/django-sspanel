# Generated by Django 2.0 on 2019-02-23 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("sspanel", "0004_auto_20190222_2209")]

    operations = [
        migrations.DeleteModel(name="PayRecord"),
        migrations.DeleteModel(name="PayRequest"),
    ]
