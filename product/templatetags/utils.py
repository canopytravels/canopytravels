from django import template
from django.contrib import admin
from order.models import Order

register = template.Library()

class CustomRequest:
    def __init__(self, user):
        self.user = user

@register.simple_tag(takes_context=True)
def get_app_list(context, **kwargs):
    custom_request = CustomRequest(context['request'].user)
    app_list = admin.site.get_app_list(custom_request)
    
    order = Order.objects.filter(read='False').count()
    return "Orders %s" %order