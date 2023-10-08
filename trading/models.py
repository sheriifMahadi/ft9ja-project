# from django.db import models
from django.contrib.auth.models import User
from djongo import models



# class Account(models.Model):
#     user_id = models.ObjectIdField()
#     firstname = models.CharField(max_length=30)
#     lastname = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
    
#     def __str__(self) -> str:
#         return f"{self.lastname} {self.firstname}"

    
# class Trade(models.Model):
#     trade_id = models.ObjectIdField()
#     owner = models.EmbeddedField(model_container=Account)
#     tradeMoney = models.DecimalField(max_digits=8, decimal_places=2)
#     profit = models.DecimalField(max_digits=8, decimal_places=2)
#     loss = models.DecimalField(max_digits=8, decimal_places=2)

#     def __str__(self) -> str:
#         return (self.user_id)