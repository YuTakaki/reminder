from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class RegisterView(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [permissions.AllowAny]
  
  def get(self, request):
    return Response({
      "test": "test"
    })

  def post(self, request):
    instance = self.serializer_class(data = request.data)
    instance.is_valid(raise_exception=True)
    user = instance.save()
    refresh = RefreshToken.for_user(user)

    return Response({
      "token": str(refresh),
      "access_token": str(refresh.access_token)
    })