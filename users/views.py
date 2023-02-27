from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import Account
from .serializers import AccountSerializer, CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# import ipdb; ipdb.set_trace()


class AccountView(APIView):
    def get(self, request: Request) -> Response:
        users = Account.objects.all()

        serializer = AccountSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        try:
            if data["is_employee"]:
                data["is_superuser"] = True
        except KeyError:
            data["is_employee"] = False

        serializer = AccountSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class SignInView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
