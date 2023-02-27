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
    movies = models.ManyToManyField(
        "users.Account",
        through="movies.MovieOrder",
        related_name="movies_orders"
    )


class MovieOrder(models.Model):
    user = models.ForeignKey(
        "users.Account",
        on_delete=models.CASCADE,
        related_name="movie_order",
    )
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_order",
    )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
    )
