from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    logo = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    pid = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=30)
    retailprice = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.URLField(max_length=200)
    logo = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return '{} {} {}'.format(str(self.pid), self.name, self.size)


class PriceHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return '{} {} {}'.format(self.item, self.date, str(self.price))
