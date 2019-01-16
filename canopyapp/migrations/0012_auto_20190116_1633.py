# Generated by Django 2.1 on 2019-01-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canopyapp', '0011_auto_20190115_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
