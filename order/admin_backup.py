from django.contrib import admin

# Register your models here.

from order.models import Order, OrderItem
from customer.models import Customer

#for sending OTP
import http.client
import json

# admin.site.register(Order)
# admin.site.register(OrderItem)


# @admin.register(OrderItem)
# class OrderAdmin(admin.ModelAdmin):
    # readonly_fields = ('stocks_available',)

    # def stocks_available(self, obj):
    #     return obj.stocks.available_quantity

    # list_display = ['order', 'product', 'pickupdatetime', 'dropdatetime']

    # list_display = ['customer', 'created_at','status', ]
    # list_filter = ['available', 'created_at']
    #list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}

#for displaying a counter along with orders
# Order._meta.verbose_name_plural = "Orders ( %s ) " % Order.objects.filter(read='False').count()



class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['duration', 'cost']
    # exclude = ['price']


def send_sms(mobile):

    # conn = http.client.HTTPConnection("api.msg91.com")

    # payload = "{ \"sender\":\"canopy\", \"SOCKET\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\": \"Message1\", \"to\": [ \"8638176825\" ] } ] }"

    # headers = {
    #     'authkey': "256624Ax2u15T0ke135c3c6465",
    #     'content-type': "application/json"
    #     }

    # conn.request("POST", "/api/v2/sendsms?country=91", payload, headers)

    # res = conn.getresponse()

    t = "123"

    conn = http.client.HTTPSConnection("control.msg91.com")

    payload = "<MESSAGE> <AUTHKEY>256624Ax2u15T0ke135c3c6465</AUTHKEY> <SENDER>CANOPY</SENDER> <ROUTE>Template</ROUTE> <CAMPAIGN>XML API</CAMPAIGN> <COUNTRY>91</COUNTRY> <SMS TEXT=\"THANK YOU FOR BOOKING\" > <ADDRESS TO=\"%s\"></ADDRESS> </SMS> </MESSAGE>" %mobile



    headers = { 'content-type': "application/xml" }

    conn.request("POST", "/api/postsms.php", payload, headers)

    res = conn.getresponse()
    data = res.read()




    # conn = http.client.HTTPConnection("api.msg91.com")
    # payload = ""
    # conn.request("POST", "/api/sendotp.php?template=&otp_length=&authkey=256624Ax2u15T0ke135c3c6465&message=&sender=&mobile="+mobile+"&otp=&otp_expiry=&email=", payload)
    # res = conn.getresponse()
    # data = res.read()
    # data_str = data.decode("utf-8")
    # data_json = json.loads(data_str)
    # return data_json


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display_links = ['id','customer']
    list_display = ['id','customer', 'status', 'created_at']
    list_filter = ['customer','completed', 'paid', 'read']
    # exclude = ['read']
    inlines = [OrderItemInline]

    readonly_fields = ['total_cost',]

    # Order._meta.verbose_name_plural = "Orders ( %s ) " % Order.objects.filter(read='False').count()


    # Method for sending sms when order is successfully completed.
    def save_model(self, request, obj, form, change):
        # obj.user = request.user
        is_completed = obj.completed
        mobile = obj.customer.customer_phone

        if is_completed:
            send_sms(mobile)
        else:
            pass
        super().save_model(request, obj, form, change)


    # METHOD FOR AUTOMATICALLY ADDING ORDER AS READ
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if obj is not None:
            obj.read = True
            obj.save()
        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)

    # class Meta:
        # verbose_name_plural = "Orders ( %s ) " % Order.objects.filter(read='False').count()




# class CustomerAdmin(admin.ModelAdmin):
#     inlines = [OrderInline,]

# admin.site.register(Customer, CustomerAdmin)


# class QuestionAdmin((admin.ModelAdmin):
#     inlines = [OptionInline,]
