from django.db import models

# Create your models here.

class Menu(models.Model):
    pie_name = models.CharField(max_length=254, null=True, blank=True)
    pie_description = models.CharField(max_length=254, null=True, blank=True)
    pie_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.pie_name