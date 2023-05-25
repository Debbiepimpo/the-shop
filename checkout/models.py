from django.db import models
from items.models import Items
from django.contrib.auth.models import User

# Create your models here.
            
class Order(models.Model):
    """customer info model for orders"""
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=75, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    remainingHours = models.IntegerField(blank=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    Item = models.ForeignKey(Items, null=False, on_delete=models.CASCADE)
    
    
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    def __str__(self):
        return "Package Id: {0}, Package: {1}, Purchase Date: {2}".format(self.id, self.Item, self.date)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    Item = models.ForeignKey(Items, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.Item.name, self.Item.udPrice)

