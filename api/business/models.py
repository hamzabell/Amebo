from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import User

# Create your models here.
class Business(models.Model):
    class Category(models.TextChoices):
        TECHNOLOGY = 'TECH', _('Technology')
        FOOD = 'FOOD', _('Food')
        COSMETIC = 'CSMT', _('Cosmetic')
        HEALTH = 'HLTH', _('Health')
        MENIAL ='MNAL', _('Menial Jobs')

    business_category = models.CharField(max_length=4, choices=Category.choices, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    name = models.CharField(max_length=255)
    pictures = models.CharField(max_length=255)

class Product(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.CharField(max_length=255)
    description = models.TextField()

class Rating(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    numberOfStars = models.IntegerField()
    comments = models.TextField()
    images = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(auto_now_add=True)