from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Substance(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class TripReport(models.Model):
    datetime_of_trip = models.DateTimeField(null=True, verbose_name="Date & time")
    location = models.CharField(max_length=100, verbose_name="Where you were")
    dosage = models.IntegerField(verbose_name="Amount")
    dosage_units = models.CharField(max_length=20, default="mg", verbose_name="Units")
    substance = models.ForeignKey(
        Substance, on_delete=models.CASCADE, verbose_name="What you took"
    )
    description = models.TextField(verbose_name='Any thoughts?', max_length=1000, null=True, blank=True)

    def __str__(self):
        return (
            f"{self.date_of_trip} - {self.substance} ({self.dosage}{self.dosage_units})"
        )
