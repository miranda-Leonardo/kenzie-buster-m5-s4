from rest_framework import serializers
from .models import Account
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["id"] = user.id

        return token


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=100,
        validators=[
            UniqueValidator(
                Account.objects.all(),
                message={"username": "username already taken."},
            )
        ],
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                Account.objects.all(),
                message={"email": "email already registered."},
            )
        ],
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(
        allow_null=True,
        default=None,
    )
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(
        allow_null=True, 
        default=False,
    )


    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(write_only=True)
