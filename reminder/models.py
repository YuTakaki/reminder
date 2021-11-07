from django.db import models
from django.db.models.deletion import CASCADE

from account.models import User

# Create your models here.
class Reminder(models.Model):
  title = models.CharField(max_length=200, null=True)
  summary = models.TextField(null=True)
  start_time = models.TimeField(default='8:00')
  end_time = models.TimeField(default='9:00')
  start_date = models.DateField()
  end_date = models.DateField(null=True)
  user = models.ForeignKey(User, related_name='reminders', on_delete=CASCADE)
  
  def __str__(self):
    return self.title