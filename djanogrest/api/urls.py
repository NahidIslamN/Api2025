from django.urls import path
from .views import users, user_details



urlpatterns = [
    path('users/', users, name='users'),
    path('users/<int:pk>/', user_details, name='user_details'),
]