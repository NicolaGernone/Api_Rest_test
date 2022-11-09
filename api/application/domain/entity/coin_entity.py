from django.db import models

class Coin(models.Model):
    sno = models.IntegerField(default=0, editable=False)
    name = models.SlugField(max_length=100000, null=False, blank=False)
    symbol = models.SlugField(max_length=5, null=False, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    hight = models.DecimalField(max_digits=100, decimal_places=10)
    low = models.DecimalField(max_digits=100, decimal_places=10)
    open = models.DecimalField(max_digits=100, decimal_places=10)
    close = models.DecimalField(max_digits=100, decimal_places=10)
    volume = models.DecimalField(max_digits=100, decimal_places=10)
    marketcap = models.DecimalField(max_digits=100, decimal_places=10)

    class Meta:
        db_table = "Coins"
        verbose_name = "Coin"
        verbose_name_plural = "Coins"