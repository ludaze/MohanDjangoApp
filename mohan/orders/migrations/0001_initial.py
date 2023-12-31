# Generated by Django 4.1.6 on 2023-08-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.SmallIntegerField()),
                ('customer_name', models.CharField(max_length=30)),
                ('truck_number', models.SmallIntegerField()),
                ('delivery_date', models.DateField()),
            ],
        ),
    ]
