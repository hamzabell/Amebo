from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    class UserType(models.TextChoices):
        BUSINESS = 'BUS', _('Business')
        REGULAR = 'REG', _('Regular')

    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=3, choices=UserType.choices, default=UserType.REGULAR)
    profile_image = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    secret_phrase = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
