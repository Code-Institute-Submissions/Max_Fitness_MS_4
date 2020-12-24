from django.db import models
from products.models import Category

# Create your models here.


class SubscriptionType(models.Model):
    name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name


class Membership(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    subscriptionType = models.ForeignKey('SubscriptionType', null=True,
                                         blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    included_extras = models.TextField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)

    def __str__(self):
        return self.name
