# Generated by Django 2.1 on 2019-01-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canopyapp', '0012_auto_20190116_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.CharField(editable=False, max_length=12, unique=True),
        ),
    ]
