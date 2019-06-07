from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=20)
    position = models.IntegerField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=10)
    price = models.IntegerField()
    description = models.CharField(max_length=120)

    def get_price(self):
        return self.code + ' has a price of ' + str(self.price)

    def _str_(self):
        return self.code
