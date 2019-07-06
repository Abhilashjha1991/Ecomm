from django.db import models

from myapp.models import Product


State_CHOICES = (
    ('0','Select'),
    ('1','New Delhi'),
    ('2','Bihar'),
    ('3','Haryana'),
    ('4','Punjab'),
    ('6','Rajasthan'),
    ('7','Utterpradesh'),
    ('8','Maharashtra'),
    ('9','Kerala'),
    ('10','Jharkhand'),
)

class Order(models.Model):
    mobile=models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=10, choices=State_CHOICES, default='Select')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=False)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
