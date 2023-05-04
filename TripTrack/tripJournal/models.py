from django.db import models

# Create your models here.


class Substance(models.Model):
    
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class TripReport(models.Model):

    date_of_trip = models.DateTimeField()
    location = models.CharField(max_length=100)
    dosage = models.IntegerField()
    dosage_units = models.CharField(max_length=20, default='mg')
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.date_of_trip.date()} - {self.substance} ({self.dosage}{self.dosage_units})"
    