from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower

class Company(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=200)
    # is_in_debt = models.BooleanField ("Is in debt ?",default=0, blank=True) TODO 

    class Meta:
        ordering = [Lower('name')]

    def __str__(self):
        return self.name

class Part(models.Model):
    number = models.CharField(max_length=20, default='None')
    description = models.CharField(max_length=100, default='None')
    location = models.CharField(max_length=10, default='None')
    count = models.CharField(max_length=10, default='None')
    price = models.CharField(max_length=10, default='None')
    type = models.CharField(max_length=10, default='None')
         
    def __str__(self):
        return self.number
    
class PriceBid(models.Model):
    class CustomerChoices(models.TextChoices):
        REGULAR = 'RG', 'Regular'
        DEALER = 'DL', 'Dealer'
        GROUP = 'GR', 'Tajmac Group'

    number = models.CharField("nabídka číslo", max_length=20, unique=True)
    parts = models.ManyToManyField(Part, related_name='parts')
    text = models.CharField(max_length=5000, blank=True)
    created_at = models.DateField(auto_now_add=True)
    customer_type = models.CharField(max_length=2, choices=CustomerChoices.choices, default='RG',)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='price_bid_counter', default='initial_company')

    class Meta:
        ordering = ['-created_at']
            # minusem pred 'created at' prohazuju poradi nejstarsi/ nejnovejsi

    def __str__(self):
        return self.number

class ServiceCase(models.Model):
    number = models.CharField(max_length=100)
    in_warranty = models.BooleanField
    description = models.CharField(max_length=1000)
    updated_by = models.ForeignKey(User, related_name='services', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='services', on_delete=models.CASCADE)

class Test(models.Model):
    nazev = models.CharField(max_length=50, default='*')
    popis =models.CharField(max_length=50, default='*')
    sklad =models.CharField(max_length=50, default='*')
    pocet =models.CharField(max_length=50, default='*')
    cena =models.CharField(max_length=50, default='*')
    typ =models.CharField(max_length=50, default='*')

    def __str__(self):
        return self.nazev