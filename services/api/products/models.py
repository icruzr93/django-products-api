from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=10)
    position = models.IntegerField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=10)
    price = models.IntegerField()
    description = models.CharField(max_length=120)

    def _str_(self):
        return self.code
