from django.db import models

# Create your models here.

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=30)
    cash_balance = models.IntegerField()

    def __str__(self):
        return self.restaurant_name

class Menu(models.Model):
    dish_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish_name

class OpenHours(models.Model):
    day = models.CharField(max_length=3)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=20)
    cash_balance = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.name

class PurchaseHistory(models.Model):
    dish_name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(max_digits=19, decimal_places=2)
    transaction_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)


