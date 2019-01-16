from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s" % (self.category_name)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

# Sub Category Model
class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_category_name

    class Meta:
        verbose_name_plural = "Sub Categories"

# Charge Category Model
class ChargeCategory(models.Model):
    charge_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.charge_category_name

    class Meta:
        verbose_name_plural = "Charge Categories"

# Product Model having relation with Category and SubCategory Models
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    product_description = models.TextField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "Products"

# Product Price Model having relation with ChargeCategory and Product
class ProductPrice(models.Model):
    charge_category_id = models.ForeignKey(ChargeCategory, on_delete=models.CASCADE, related_name='charges_category')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pid')
    charge = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        verbose_name_plural = "Product Prices"

# Stocks Model having relation with Product
class Stocks(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="stocks")
    net_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    flash_sale = models.BooleanField()

    class Meta:
        verbose_name_plural = "Stocks"

# Maintenance Model having relation with Product
class Maintenance(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity_in_maintenance = models.IntegerField()

    class Meta:
        verbose_name_plural = "Maintenance"


# Customer Model
class Customer(models.Model):
    customer_name = models.CharField(max_length=40)
    customer_phone = models.CharField(max_length=12, unique=True)
    customer_email = models.CharField(max_length =300, null = True)
    customer_address = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name

#New models
class Cart(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.customer, self.count, self.total)

class Entry(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete='CASCADE')
    cart = models.ForeignKey(Cart, null=True, on_delete='CASCADE')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product.product_name)

@receiver(post_save, sender=Entry)
def update_cart(sender, instance, **kwargs):
    #line_cost = instance.quantity * instance.product.cost
    line_cost = 100
    instance.cart.total += line_cost
    #instance.cart.count += instance.quantity
    instance.cart.count += 11
    instance.cart.updated = datetime.now()




# Booking Model having realtion with Customer, Product, ChargeCategory models
# class Booking(models.Model):
#     booking_id = models.CharField(max_length=50)
#     customer_id = models.ManyToManyField(Customer)
#     product_id = models.ManyToManyField(Product)
#     quantity_booked = models.IntegerField()
#     booking_type = models.ForeignKey(ChargeCategory, on_delete=models.CASCADE)
#     datetime_from = models.DateTimeField(auto_now=False)
#     datetime_to = models.DateTimeField(auto_now=False)
#     booking_cost = models.DecimalField(max_digits=20, decimal_places=2, editable=True)





#    def save(self, *args, **kwargs):
        #Booking.save(self,*args, **kwargs)
        #data =  ProductPrice.objects.get(product_id=self.product_id)
#        data = 20
#        self.booking_cost = data
        #self.booking_cost.add(data)
#        super(Booking, self).save(*args, **kwargs)

    #computed = models.CharField(max_length=32, editable=False)

    #commented for concept
#   ''' def save(self, *args, **kwargs):
#        self.computed = self. + self.y
#        super(TestModel, self).save(*args, **kwargs)
#        '''

# BookingStatusCategory Model
class BookingStatusCategory(models.Model):
    status_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Booking Status Categories"

# BookingStatus Model having relation with Booking, BookingStatusCategory models
# class BookingStatus(models.Model):
#     booking_id = models.OneToOneField(Booking, on_delete=models.CASCADE)
#     booking_status = models.ForeignKey(BookingStatusCategory, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "Booking Status"