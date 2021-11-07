from rest_framework import generics, permissions
from rest_framework.response import Response

from reminder.models import Reminder
from .serializers import ReminderSerializer

# Create your views here.
class RemindersView(generics.GenericAPIView):
  serializer_class = ReminderSerializer
  permission_classes = [permissions.IsAuthenticated]
  lookup_url_kwarg = "id"

  def post(self, request):
    instance = self.get_serializer(data = request.data)
    instance.is_valid(raise_exception=True)
    instance.save()
    
    return Response({
      "msg" : instance.data
    })

  def get(self, request):
    month = request.query_params.get('month')
    year = request.query_params.get('year')
    reminders = Reminder.objects.filter(start_date__month = month, start_date__year = year)
    serializers = self.get_serializer(reminders, many=True)
    
    return Response({
      'results' : serializers.data
      
    })

  def delete(self, request, id):
    reminder = Reminder.objects.filter(id = id).first()
    deleted = self.get_serializer(reminder)
    reminder.delete()
    return Response({
      'deleted' : deleted.data
    })

  def put(self, request, id):
    data = request.data
    reminder = Reminder.objects.get(id = id)
    reminder.title = data.get('title')
    reminder.summary = data.get('summary')
    reminder.start_time = data.get('start_time')
    reminder.end_time = data.get('end_time')
    reminder.start_date = data.get('start_date')
    reminder.end_date = data.get('end_date')
    reminder.save()
    instance = self.get_serializer(reminder)

    return Response({
      "msg" : instance.data
    })



class ReminderListView(generics.GenericAPIView):
  serializer_class = ReminderSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    date = request.query_params.get('date')
    reminders = Reminder.objects.filter(start_date = date)
    serializers = ReminderSerializer(reminders, many=True)
    
    return Response({
      'results' : serializers.data
    })