from rest_framework import generics, permissions

from .models import User
from .serializers import LoginSerializers, RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.
class UserView(generics.GenericAPIView):
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = self.get_serializer(request.user)

    return Response({
      'user': user.data
    })

class RegisterView(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [permissions.AllowAny]
  

  def post(self, request):
    instance = self.get_serializer(data = request.data)
    instance.is_valid(raise_exception=True)
    user = instance.save()
    refresh = RefreshToken.for_user(user)
    user = UserSerializer(user)
    return Response({
      "user": user.data,
      "token": str(refresh),
      "access_token": str(refresh.access_token)
    })

class LoginView(generics.GenericAPIView):
  serializer_class = LoginSerializers
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    email = request.data["email"]
    password = request.data['password']
    user = User.objects.filter(email = email).first()
    if user is None:
      raise AuthenticationFailed('no username')
    if not user.check_password(password):
      raise AuthenticationFailed('Wrong password')
    
    refresh = RefreshToken.for_user(user)
    user = UserSerializer(user)
    return Response({
      "user" : user.data,
      "token": str(refresh),
      "access_token": str(refresh.access_token)
    })