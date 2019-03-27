from django.db import models
from django.urls import reverse


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,
                            unique=True)

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])

    def __unicode__(self):
        return u"%s" % (self.category_name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

# Sub Category Model
class SubCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,
                            unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sub Categories"

# Product Model having relation with Category and SubCategory Models
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="product_subcategory")
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    description = models.TextField()
    price_default = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_hour = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    price_day = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    price_week = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    available = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"
        ordering = ('name',)
        index_together = (('id', 'slug'),)



# INVENTORY MANAGEMENT PART**************
class Stocks(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="stocks")
    net_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    flash_sale = models.BooleanField()

    class Meta:
        verbose_name_plural = "Stocks"

class Maintenance(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity_in_maintenance = models.IntegerField()

    class Meta:
        verbose_name_plural = "Maintenance"
