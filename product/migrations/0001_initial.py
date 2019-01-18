# Generated by Django 2.1 on 2019-01-18 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_in_maintenance', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Maintenance',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('price_default', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('price_hour', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('price_day', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('price_week', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('available', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.Category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_quantity', models.IntegerField()),
                ('available_quantity', models.IntegerField()),
                ('flash_sale', models.BooleanField()),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='product.Product')),
            ],
            options={
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_subcategory', to='product.SubCategory'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='product_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
