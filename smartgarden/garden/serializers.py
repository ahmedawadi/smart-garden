from rest_framework import serializers
from .models import Garden, GardenInfo


class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ["id", "name"]


class GardenInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenInfo
        fields = [
            "garden",
            "light_intensity",
            "soil_moisture",
            "humidity",
            "co2_level",
            "soil_pH",
        ]
