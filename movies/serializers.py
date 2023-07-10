from rest_framework import serializers
from movies.models import Movie



class MovieSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> Movie:
        movie_obj = Movie.objects.create(**validated_data)
        return movie_obj

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]

        read_only_fields = ["id", "user"]