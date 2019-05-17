from django.db import models

# Create your models here.
class Size(models.Model):
    tittle = models.CharField(max_length=100)

    def __str__(self):
        return self.tittle

class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size,models.CASCADE)
