from rest_framework import generics, permissions
from .serializers import LoginSerializers, RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class RegisterView(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [permissions.AllowAny]
  

  def post(self, request):
    instance = self.get_serializer(data = request.data)
    instance.is_valid(raise_exception=True)
    user = instance.save()
    refresh = RefreshToken.for_user(user)

    return Response({
      "token": str(refresh),
      "access_token": str(refresh.access_token)
    })

class LoginView(generics.GenericAPIView):
  serializer_class = LoginSerializers
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    email = request.data["email"]
    password = request.data['password']
    return Response({
      "token": str(email),
      "access_token": str(password)
    })