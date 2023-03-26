from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class WalletAccount(models.Model):
    wallet_user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField()


class WalletUser(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
