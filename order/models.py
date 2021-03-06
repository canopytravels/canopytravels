import math
from datetime import datetime
from decimal import Decimal
from django.db import models
from customer.models import Customer
from product.models import Product


#New models
class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE, related_name="customer_orders")
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default="booked")
    read = models.BooleanField(default=False)

    # def __str__(self):
    #     return "User: {} has {} items in their cart. Their total is ${}".format(self.customer, self.count, self.total)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_orderitems.all())

    total_cost = property(get_total_cost)

class OrderItem(models.Model):
    DEFAULT = 'DF'
    HOURLY = 'HR'
    DAILY = 'DY'
    WEEKLY = 'WK'
    ORDER_TYPE_CHOICES = (
        (DEFAULT, 'Default'),
        (HOURLY, 'Hourly'),
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
    )
    order_type = models.CharField(
        max_length=2,
        choices=ORDER_TYPE_CHOICES,
        default=DEFAULT,
    )

    product = models.ForeignKey(Product, null=True, on_delete='CASCADE', related_name="product_orderitems")
    order = models.ForeignKey(Order, null=True, on_delete='CASCADE', related_name="order_orderitems")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    pickupdatetime = models.DateTimeField()
    dropdatetime = models.DateTimeField()

    #calculate duration
    # elif order_type == 'HR':
    #     duration = duration_diff.seconds/3600
    # elif order_type == 'WK':
    #     duration = duration_diff.days/7
    #end of calculation

    def __str__(self):
        return '{}'.format(self.id)

    # custom property method for calculating duration
    def get_duration(self):
        start_date_str = self.pickupdatetime.strftime("%Y-%m-%d %H:%M")
        end_date_str = self.dropdatetime.strftime("%Y-%m-%d %H:%M")

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M")
        duration_diff = end_date - start_date

        if self.order_type == 'HR':
            duration = duration_diff.seconds/3600
        elif self.order_type == 'DY':
            if duration_diff.days == 0 and duration_diff.seconds != 0 and duration_diff.seconds/3600>15:
                duration = duration_diff.days+1
            elif duration_diff.days>0 and duration_diff.seconds>0:
                duration = duration_diff.days+1
            else:
                duration = duration_diff.days
        elif self.order_type == 'WK':
            duration = math.ceil(duration_diff.days/7)
        else:
            duration = 1
        return duration

    def get_cost(self):
        return Decimal(self.price) * Decimal(self.quantity) * Decimal(self.get_duration())

    #property fields for displaying in the Admin panel
    cost = property(get_cost)
    duration = property(get_duration)


# @receiver(post_save, sender=Entry)
# def update_cart(sender, instance, **kwargs):
#     #line_cost = instance.quantity * instance.product.cost
#     line_cost = 100
#     instance.cart.total += line_cost
#     #instance.cart.count += instance.quantity
#     instance.cart.count += 11
#     instance.cart.updated = datetime.now()