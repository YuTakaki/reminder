
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('reminder.urls')),
]
