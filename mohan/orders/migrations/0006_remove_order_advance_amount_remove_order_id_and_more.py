# Generated by Django 4.1.6 on 2023-08-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_delivery_date_order_order_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='advance_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='deposit_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='desc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='price_per_item',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
