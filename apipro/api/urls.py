from django.urls import path
from api.views import users, userdetails


urlpatterns = [
    path('users/', users, name='users'),
    path('user-details/<int:pk>/', userdetails, name='user-details'),
]
