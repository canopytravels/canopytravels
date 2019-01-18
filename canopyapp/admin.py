from django.contrib import admin

# Register your models here.
#from canopyapp.models import Category, SubCategory, ChargeCategory
#from canopyapp.models import Product, ProductPrice, Stocks, Maintenance
#from canopyapp.models import Booking, BookingStatusCategory, BookingStatus



# from django.utils.datetime_safe import datetime

# from canopyapp.models import  Cart, Entry

# class EntryAdmin(admin.ModelAdmin):
#     # Overide of the save model
#     def save_model(self, request, obj, form, change):
#         #obj.cart.total += obj.quantity * obj.product.cost
#         obj.cart.total += obj.quantity * 0
#         obj.cart.count += obj.quantity
#         obj.cart.updated = datetime.now()
#         obj.cart.save()
#         super().save_model(request, obj, form, change)

# # Register your models here.
# admin.site.register(Product)
# admin.site.register(Cart)
# admin.site.register(Entry, EntryAdmin)

# class ProductPriceInline(admin.TabularInline):
#     model = ProductPrice

# class ProductAdmin(admin.ModelAdmin):
#     inlines = [
#         ProductPriceInline,
#     ]

# admin.site.register(Category)
# admin.site.register(SubCategory)
# admin.site.register(ChargeCategory)
# # admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductPrice)
# admin.site.register(Stocks)
# admin.site.register(Maintenance)
#admin.site.register(Customer)
# admin.site.register(Booking)
# admin.site.register(BookingStatusCategory)
# admin.site.register(BookingStatus)