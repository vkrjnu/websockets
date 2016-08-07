from django.db import models

# Create your models here.


class Fibonacci(models.Model):
    num = models.BigIntegerField(default=1)
    output = models.DecimalField(max_digits=50,decimal_places=1,default=0.0)
