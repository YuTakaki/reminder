from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'id']
    

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password']

  def create(self, data):
    password = data.pop('password', None)
    instance = self.Meta.model(**data)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance

class LoginSerializers(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'password']
