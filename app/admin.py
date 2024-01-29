from django.contrib import admin
from app.models import Customer, Vendor, DeliveryPerson, SystemManager
from app.models import Food, Cart, CartItem, Order, OrderItem, Payment

admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(DeliveryPerson)
admin.site.register(SystemManager)
admin.site.register(Food)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
