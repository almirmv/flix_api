from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    # campo calculado
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    # metodo para o campo calculado. padaro "def_nomedocampocalculado(self, obj)
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))
        if rate:
            return round(rate, 1)
        return None

    # padrao de validate é "def validate_nomedacolunadodb(self,value)"
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value  # nao deu erro simplesmente retorna o value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não pode ser maior que 200 caracteres')
        return value


class MovieStatsSerilizer(serializers.Serializer):
    # validacoes
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
