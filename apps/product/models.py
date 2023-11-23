from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


# [NOTE] Use in place of sessions for the select functionality
# class ProductSelected(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
#     selected = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return f"{self.user} selected {self.product}"
