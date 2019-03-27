from datetime import datetime
from decimal import Decimal
from django.conf import settings
from product.models import Product

class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # METHOD FOR ADDING ADDONS TO THE CART
    def add_addons(self, product, quantity=0, update_quantity=False):
        addons_id = str(product.id)
        if addons_id not in self.cart:
            self.cart[addons_id] = self.cart[addons_id] = {'quantity': 0, 'price': str(product.price_default), 'order_type':'DF', 'pickup':'2000-01-01 10:00', 'drop':'2000-01-01 10:00', 'duration': 1, 'category': str(product.category)}
        if update_quantity:
            self.cart[addons_id]['quantity'] = quantity
        else:
            self.cart[addons_id]['quantity'] += quantity
        self.save()
    # END OF METHOD OF ADDING ADDONS TO THE CART


    # METHOD FOR ADDING VEHICLES INTO THE CART
    def add(self, product, order_type, pickup, drop, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """

        #calculate duratin
        start_date = datetime.strptime(pickup, "%Y-%m-%d %H:%M")
        end_date = datetime.strptime(drop, "%Y-%m-%d %H:%M")
        duration = end_date-start_date

        #end of calculation

        product_id = str(product.id)
        product_category = str(product.category)
        if product_id not in self.cart:
            if order_type == 'HR':
                self.cart[product_id] = {'quantity': 1, 'price': str(product.price_hour), 'order_type':order_type, 'pickup':pickup, 'drop':drop, 'duration':duration.seconds/3600, 'total_price':str(Decimal(product.price_hour) * Decimal(duration.seconds/3600)), 'category': product_category}
            elif order_type == 'DY':
                if duration.days == 0 and duration.seconds != 0 and duration.seconds/3600>15:
                    self.cart[product_id] = {'quantity': 1, 'price': str(product.price_day), 'order_type':order_type, 'pickup':pickup, 'drop':drop, 'duration':duration.days+1, 'total_price':str(Decimal(product.price_day) * Decimal(duration.days+1)), 'category': product_category}
                elif duration.days>0 and duration.seconds>0:
                    self.cart[product_id] = {'quantity': 1, 'price': str(product.price_day), 'order_type':order_type, 'pickup':pickup, 'drop':drop, 'duration':duration.days+1, 'total_price':str(Decimal(product.price_day) * Decimal(duration.days+1)), 'category': product_category}
                else:
                    self.cart[product_id] = {'quantity': 1, 'price': str(product.price_day), 'order_type':order_type, 'pickup':pickup, 'drop':drop, 'duration':duration.days, 'total_price':str(Decimal(product.price_day) * Decimal(duration.days)), 'category': product_category}
            elif order_type == 'WK':
                self.cart[product_id] = {'quantity': 1, 'price': str(product.price_week), 'order_type':order_type, 'pickup':pickup, 'drop':drop, 'duration':duration.days/7, 'total_price':str(Decimal(product.price_week) * Decimal(duration.days/7)), 'category': product_category}
            else:
                self.cart[product_id] = {'quantity': 1, 'price': str(product.price_hour), 'order_type':order_type, 'pickup':pickup, 'drop':drop}

        if update_quantity and (product_category!='BIKES' or product_category!='CARS') :
        # if update_quantity:
            # self.cart[product_id]['quantity'] = quantity
            self.cart[product_id]['quantity'] += quantity
        else:
            # self.cart[product_id]['quantity'] += quantity
            self.cart[product_id]['quantity'] = quantity
        self.save()

    # def add(self, product, quantity=1, update_quantity=False):
    #     """
    #     Add a product to the cart or update its quantity.
    #     """
    #     product_id = str(product.id)
    #     if product_id not in self.cart:
    #         self.cart[product_id] = {'quantity': 0,
    #                                   'price': str(product.price_hour)}
    #     if update_quantity:
    #         self.cart[product_id]['quantity'] = quantity
    #     else:
    #         self.cart[product_id]['quantity'] += quantity
    #     self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            if item['duration']!=None:
                item['total_price'] = Decimal(item['price']) * item['quantity'] * Decimal(item['duration'])
            else:
                item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
         return sum(Decimal(item['price']) * item['quantity'] * Decimal(item['duration']) for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()