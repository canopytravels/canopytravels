# Generated by Django 2.1 on 2018-12-31 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=50)),
                ('quantity_booked', models.IntegerField()),
                ('datetime_from', models.DateTimeField(auto_now=True)),
                ('datetime_to', models.DateTimeField(auto_now=True)),
                ('booking_cost', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='canopyapp.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='BookingStatusCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=40)),
                ('customer_phone', models.CharField(max_length=12)),
                ('customer_email', models.CharField(max_length=300)),
                ('customer_address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_in_maintenance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('product_description', models.TextField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canopyapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge', models.DecimalField(decimal_places=2, max_digits=20)),
                ('charge_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canopyapp.ChargeCategory')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canopyapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_quantity', models.IntegerField()),
                ('available_quantity', models.IntegerField()),
                ('flash_sale', models.BooleanField()),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='canopyapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canopyapp.SubCategory'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='product_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='canopyapp.Product'),
        ),
        migrations.AddField(
            model_name='bookingstatus',
            name='booking_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canopyapp.BookingStatusCategory'),
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canopyapp.ChargeCategory'),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer_id',
            field=models.ManyToManyField(to='canopyapp.Customer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='product_id',
            field=models.ManyToManyField(to='canopyapp.Product'),
        ),
    ]
