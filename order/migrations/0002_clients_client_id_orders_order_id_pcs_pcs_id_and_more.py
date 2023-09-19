# Generated by Django 4.2.2 on 2023-09-15 02:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="clients",
            name="client_id",
            field=models.TextField(default="", unique=True),
        ),
        migrations.AddField(
            model_name="orders",
            name="order_id",
            field=models.TextField(default="", unique=True),
        ),
        migrations.AddField(
            model_name="pcs",
            name="pcs_id",
            field=models.TextField(default="", unique=True),
        ),
        migrations.AddField(
            model_name="salespeople",
            name="salesperson_id",
            field=models.TextField(default="", unique=True),
        ),
        migrations.AlterField(
            model_name="orders",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orders",
            name="notice",
            field=models.TextField(blank=True, null=True),
        ),
    ]