from tea_app.models import Colors, Teas
from rest_framework import serializers

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ["color_id", "name"]

class TeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teas
        fields = ["tea_id", "name", "description", "color", "countries"]