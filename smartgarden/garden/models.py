from django.db import models
import uuid


# Create your models here.
class Garden(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=400)


class GardenInfo(models.Model):
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    light_intensity = models.DecimalField(max_digits=10, decimal_places=2)
    soil_moisture = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    co2_level = models.DecimalField(max_digits=5, decimal_places=2)
    soil_pH = models.DecimalField(max_digits=5, decimal_places=2)
