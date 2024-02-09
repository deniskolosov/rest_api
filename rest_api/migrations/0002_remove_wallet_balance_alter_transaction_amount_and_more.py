# Generated by Django 5.0.2 on 2024-02-09 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rest_api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wallet",
            name="balance",
        ),
        migrations.AlterField(
            model_name="transaction",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="wallet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transactions",
                to="rest_api.wallet",
            ),
        ),
    ]
