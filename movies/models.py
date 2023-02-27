from django.db import models


class Rates(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(
        max_length=10,
        null=True,
        default=None,
    )
    rating = models.CharField(
        max_length=20,
        choices=Rates.choices,
        default=Rates.G,
    )
    synopsis = models.CharField(
        max_length=200,
        null=True,
        default=None,
    )
    user = models.ForeignKey(
        "users.Account",
        on_delete=models.CASCADE,
        related_name="movie",
    )
