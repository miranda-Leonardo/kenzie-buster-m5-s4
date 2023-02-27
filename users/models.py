from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.CharField(
        max_length=127,
        unique=True,
        error_messages={
            "message": "email already registred.",
        },
    )
    username = models.CharField(
        unique=True,
        max_length=150,
        error_messages={
            "message": "username already taken.",
        },
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    is_employee = models.BooleanField(
        null=True,
        default=False,
    )
    is_superuser = models.BooleanField(
        null=True, 
        default=False,
    )

    
    def __repr__(self) -> str:
        return f"<user [{self.id}] - {self.email}>"
