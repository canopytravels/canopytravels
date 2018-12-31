from django.db import models

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=50)

# Sub Category Model
class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=50)

# Charge Category Model
class ChargeCategory(models.Model):
    charge_category_name = models.CharField(max_length=50)

# Product Model having relation with Category and SubCategory Models
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=False, blank=False)
    product_description = models.TextField()

# Product Price Model having relation with ChargeCategory and Product
class ProductPrice(models.Model):
    charge_category_id = models.ForeignKey(ChargeCategory, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    charge = models.DecimalField(max_digits=20, decimal_places=2)

# Stocks Model having relation with Product
class Stocks(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    net_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    flash_sale = models.BooleanField()

# Maintenance Model having relation with Product
class Maintenance(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity_in_maintenance = models.IntegerField()



# Customer Model
class Customer(models.Model):
    customer_name = models.CharField(max_length=40)
    customer_phone = models.CharField(max_length=12)
    customer_email = models.CharField(max_length =300)
    customer_address = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

# Booking Model having realtion with Customer, Product, ChargeCategory models
class Booking(models.Model):
    booking_id = models.CharField(max_length=50)
    customer_id = models.ManyToManyField(Customer)
    product_id = models.ManyToManyField(Product)
    quantity_booked = models.IntegerField()
    booking_type = models.ForeignKey(ChargeCategory, on_delete=models.CASCADE)
    datetime_from = models.DateTimeField(auto_now=True)
    datetime_to = models.DateTimeField(auto_now=True)
    booking_cost = models.DecimalField(max_digits=20, decimal_places=2)

# BookingStatusCategory Model
class BookingStatusCategory(models.Model):
    status_name = models.CharField(max_length=50)

# BookingStatus Model having relation with Booking, BookingStatusCategory models
class BookingStatus(models.Model):
    booking_id = models.OneToOneField(Booking, on_delete=models.CASCADE)
    booking_status = models.ForeignKey(BookingStatusCategory, on_delete=models.CASCADE)