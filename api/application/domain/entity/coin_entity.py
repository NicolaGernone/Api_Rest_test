from django.db import models

class Coin(models.Model):
    sno = models.IntegerField(default=0, editable=False)
    name = models.SlugField(max_length=100000, null=False, blank=False)
    symbol = models.SlugField(max_length=5, null=False, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    hight = models.DecimalField(max_digits=None, decimal_places=None)
    low = models.DecimalField(max_digits=None, decimal_places=None)
    open = models.DecimalField(max_digits=None, decimal_places=None)
    close = models.DecimalField(max_digits=None, decimal_places=None)
    volume = models.DecimalField(max_digits=None, decimal_places=None)
    marketcap = models.DecimalField(max_digits=None, decimal_places=None)

    class Meta:
        db_table = "Coins"
        verbose_name = "Coin"
        verbose_name_plural = "Coins"
        name = 'Name'
        symbol = 'Symbol'
        sno = 'SNo'