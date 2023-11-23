from django.contrib.auth import login, logout

from rest_framework import generics, permissions, views, status
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request) -> Response:
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(user.email, status=status.HTTP_202_ACCEPTED)


class LogoutView(views.APIView):
    def post(self, request) -> Response:
        logout(request)
        return Response(status=status.HTTP_200_OK)
