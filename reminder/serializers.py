from rest_framework import serializers
from account.models import User
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
  class Meta:
    model = Reminder
    fields = '__all__'
    extra_kwargs = {
      "user": {
        'read_only' : True
      }
    }