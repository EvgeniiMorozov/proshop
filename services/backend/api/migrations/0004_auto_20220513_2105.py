# Generated by Django 3.2.13 on 2022-05-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_product_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="created_at",
            new_name="createdAt",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="delivered_at",
            new_name="deliveredAt",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="is_delivered",
            new_name="isDelivered",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="is_paid",
            new_name="isPaid",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="paid_at",
            new_name="paidAt",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="shipping_price",
            new_name="shippingPrice",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="tax_price",
            new_name="taxPrice",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="total_price",
            new_name="totalPrice",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="count_in_stock",
            new_name="countInStock",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="created_at",
            new_name="createdAt",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="num_reviews",
            new_name="numReviews",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="postal_code",
            new_name="postalCode",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="shipping_price",
            new_name="shippingPrice",
        ),
    ]
