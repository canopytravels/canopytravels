from django.db import models


# Customer Model
class Customer(models.Model):
    customer_name = models.CharField(max_length=40)
    customer_phone = models.CharField(max_length=12, unique=True)
    customer_email = models.CharField(max_length =300, null = True)
    customer_address = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name
