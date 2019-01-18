from django.contrib import admin

# Register your models here.

from product.models import Category, SubCategory, Product, Stocks, Maintenance

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Stocks)
admin.site.register(Maintenance)
