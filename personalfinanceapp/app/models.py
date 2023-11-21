from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# Investment Types
class InvestmentType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Institutions
class Institution(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


# Portfolio that holds all instruments
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Instrument (eg. cash, stocks)
class Instrument(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    investment_type = models.ForeignKey(InvestmentType, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    ticker_symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    position = models.DecimalField(max_digits=12, decimal_places=2)
    market_value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.ticker_symbol}"
