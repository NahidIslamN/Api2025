from django.urls import path
from api.views import getuser, create_user



urlpatterns = [
    path('users/', getuser),
    path('users/create_user/', create_user),
    
]
