from django.db import models


class RoleTypeChoices(models.TextChoices):
    guest = 'Guest'
    seller = 'Seller'
    manager = 'Manager'
    admin = 'Admin'


class AccountTypeChoices(models.TextChoices):
    basic = 'Basic'
    prime = 'Prime'
