# Generated by Django 3.2.13 on 2022-04-14 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "_id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                (
                    "payment_method",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "tax_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                (
                    "shipping_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                ("is_paid", models.BooleanField(default=False)),
                ("paid_at", models.DateTimeField(blank=True, null=True)),
                ("is_delivered", models.BooleanField(default=False)),
                ("delivered_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShippingAddress",
            fields=[
                (
                    "_id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                ("city", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "postal_code",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("country", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "shipping_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                (
                    "order",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.order",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "_id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("rating", models.IntegerField(blank=True, default=0, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "_id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("qty", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                ("image", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.product",
                    ),
                ),
            ],
        ),
    ]
