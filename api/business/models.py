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
    business_name = models.CharField(max_length=255)
    pictures = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.business_name

class Product(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.product_name

class Rating(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, default=None, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    numberOfStars = models.IntegerField()
    comment = models.TextField()
    images = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.numberOfStars)