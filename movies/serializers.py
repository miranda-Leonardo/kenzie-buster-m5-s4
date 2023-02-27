from rest_framework import serializers
from .models import Movie, Rates


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        allow_null=True,
        default=None,
    )
    rating = serializers.ChoiceField(
        choices=Rates.choices,
        default=Rates.G,
    )
    synopsis = serializers.CharField(
        allow_null=True,
        default=None,
    )
    added_by = serializers.CharField(
        source="user.email", 
        read_only=True,
    )


    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
