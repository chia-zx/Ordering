"""
Definition of models.
"""

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#sharing entity

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_name = models.CharField(max_length=30, null=True)
    customer_phone = models.CharField(max_length=20, null=True)
    customer_address = models.CharField(max_length=200, null=True)
    customer_spent = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    def __str__(self):
        return str(self.customer_id)

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vendor_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    vendor_name = models.CharField(max_length=30, null=True)
    vendor_phone = models.CharField(max_length=20, null=True)
    vendor_address = models.CharField(max_length=200, null=True)
    vendor_revenue = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    def __str__(self):
        return str(self.vendor_id)
    
class DeliveryPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    deliveryperson_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    deliveryperson_name = models.CharField(max_length=30, null=True)
    deliveryperson_phone = models.CharField(max_length=20, null=True)
    deliveryperson_address = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.deliveryperson_id)
    
class SystemManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    manager_name = models.CharField(max_length=30, null=True)
    def __str__(self):
        return str(self.manager_id)
    
class Food(models.Model):
    food_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    food_name = models.CharField(max_length=30)
    food_description = models.CharField(max_length=200, null=True, default=None, blank=True)
    food_price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    food_available = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    vendor_id =  models.ForeignKey(Vendor, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.food_id)

class Cart(models.Model):
    cart_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    cart_date = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.cart_id)
    
class CartItem(models.Model):
    cartitem_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    cartitem_quantity = models.IntegerField()
    def __str__(self):
        return str(self.cartitem_id)
    def get_food_info(self):
        # Access information about the associated Food, even if it's deleted
        if self.food_id:
            return {
                'food_name': self.food_id.food_name,
                'food_description': self.food_id.food_description,
                'food_price': self.food_id.food_price,
                'food_available': self.food_id.food_available,
                'vendor_id': self.food_id.vendor_id
            }
        else:
            return None

class Order(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Delivering', 'Delivering'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Rejected', 'Rejected'),
    ]

    order_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order_date = models.DateTimeField(auto_now_add=True)
    order_totalprice = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=STATUS)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deliveryperson_id = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.order_id)
    
class OrderItem(models.Model):
    orderitem_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    orderitem_quantity = models.IntegerField()
    def __str__(self):
        return str(self.orderitem_id)
    
class Payment(models.Model):
    STATUS = [
        ('Success', 'Success'),
        ('Fail', 'Fail'),
    ]
    payment_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=STATUS)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.payment_id)
