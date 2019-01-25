from django.contrib import admin
from django.contrib.auth.models import User, Group
# Register your models here.

from product.models import Category, SubCategory, Product, Stocks, Maintenance



admin.site.unregister(User)
admin.site.unregister(Group)

# admin.site.register(Stocks)
admin.site.register(Maintenance)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('stocks_available',)

    def stocks_available(self, obj):
        return obj.stocks.available_quantity

    list_display = ['name', 'slug','category','subcategory', 'price_default','price_hour','price_day','price_week',
                    'available','stocks_available', 'created_at']
    list_filter = ['available', 'created_at']
    #list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'net_quantity', 'available_quantity', 'flash_sale']
    list_editable = ['net_quantity', 'available_quantity', 'flash_sale']
