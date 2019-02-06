from django.db import models
from customer.models import Customer
from product.models import Product

#New models
class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE, related_name="customer_orders")
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default="booked")

    # def __str__(self):
    #     return "User: {} has {} items in their cart. Their total is ${}".format(self.customer, self.count, self.total)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_orderitems.all())




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
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    pickupdatetime = models.DateTimeField()
    dropdatetime = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


# @receiver(post_save, sender=Entry)
# def update_cart(sender, instance, **kwargs):
#     #line_cost = instance.quantity * instance.product.cost
#     line_cost = 100
#     instance.cart.total += line_cost
#     #instance.cart.count += instance.quantity
#     instance.cart.count += 11
#     instance.cart.updated = datetime.now()