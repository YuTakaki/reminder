from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('', views.UserView.as_view()),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view())
]
