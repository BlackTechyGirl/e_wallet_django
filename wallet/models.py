import email

from django.contrib.auth.models import User, AbstractUser
from django.db import models, transaction
from django.template.defaultfilters import default


# Create your models here.

class NextOfKin(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    bvn = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class CreditCard(models.Model):
    card_name = models.CharField(max_length=255, blank=False, null=False)
    card_number = models.CharField(max_length=10, blank=False)
    expiry_date = models.DateField(null=False, blank=False)
    cvv = models.IntegerField()

    def __str__(self):
        return self.card_name


class Account(models.Model):
    BANK_CHOICES = [
        ('ZENITH', 'ZENITH'),
        ('UBA', 'UBA'),
        ('PALMPAY', 'PALMPAY'),
        ('KUDA', 'KUDA'),
        ('GTB', 'GTB'),
    ]
    name = models.CharField(max_length=255, blank=False, null=False)
    account_number = models.CharField(max_length=255, blank=False, null=False)
    bank = models.CharField(max_length=255, choices=BANK_CHOICES, default='')
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name


class WalletUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    nin = models.CharField(blank=False, null=False, max_length=225)
    home_address = models.CharField(blank=False, null=False, max_length=225)
    # next_of_kin = models.ForeignKey(NextOfKin, on_delete=models.CASCADE,
    #                                 related_name='next_of_kin')
    # credit_card = models.ForeignKey(CreditCard, on_delete=models.PROTECT, blank=False, null=False,
    #                                 related_name='credit_cards')


class Airtime(models.Model):
    NETWORK_CHOICES = [
        ('MTN', 'MTN'),
        ('GLO', 'GLO'),
        ('AIRTEL', 'AIRTEL'),
        ('ETISALAT', 'ETISALAT'),
    ]
    network = models.CharField(max_length=25, choices=NETWORK_CHOICES, default='')
    phone_number = models.CharField(max_length=255, blank=False, null=False)


class Transaction(models.Model):
    STATUS = [
        ('SUCCESSFUL', 'SUCCESSFUL'),
        ('FAILED', 'FAILED'),
        ('REVERSED', 'REVERSED'),
        ('PENDING', 'PENDING'),
    ]
    TRANSACTION_TYPES = [
        ('WITHDRAWN', 'WITHDRAWN'),
        ('SPENDING', 'SPEND'),
        ('SAVE', 'SAVE'),
        ('AIRTIME', 'AIRTIME'),
    ]
    transaction_types = models.CharField(max_length=24, choices=TRANSACTION_TYPES, default='')
    status = models.CharField(max_length=25, choices=STATUS, default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default='')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    transaction_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(WalletUser, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.transaction_types


class Wallet(models.Model):
    user = models.ForeignKey(WalletUser, on_delete=models.CASCADE, related_name='wallet_user')
    balance = models.DecimalField(decimal_places=4, default=0, max_digits=6)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.user
