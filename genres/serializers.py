from rest_framework import serializers
from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre       # qual modelo
        fields = '__all__'  # quais campos para serializar
