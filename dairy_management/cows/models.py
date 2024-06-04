from django.db import models
from django.contrib.auth.models import User

class Cow(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    milk_production = models.FloatField(help_text="Milk production in litres")
    weight = models.FloatField(help_text="Weight in kilograms")
    health = models.TextField()

    def __str__(self):
        return self.name

class MilkRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, related_name='milk_records')
    date = models.DateField()
    quantity = models.FloatField(help_text="Milk quantity in litres")

    class Meta:
        unique_together = ('cow', 'date')

    def __str__(self):
        return f"{self.cow.name} - {self.date}: {self.quantity} litres"