from django.urls import path
from . import views

urlpatterns = [
  path('reminders', views.RemindersView.as_view()),
  path('reminders/<int:id>', views.RemindersView.as_view())
]
