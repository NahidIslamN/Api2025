from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import User
from api.serializer import UserSerializer
import requests
from django.http import JsonResponse  




# Create your views here.


def index(request):
    url = "http://127.0.0.1:8000/users"  # Replace with the actual API URL
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON
       
  
        
    return render(request, 'index.html', {'data': data})






@api_view(['GET', 'POST',"PUT"])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(UserSerializer({"username":"user01", 'email':"email@gmai.com", 'password':'14156',"first_name":'nahid','last_name':"islam"}).data)
        

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PUT":
        user = User.objects.get(id=request.data['id'])
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',"DELETE"])    
def userdetails(request,pk):
    if request.method == "DELETE":
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "GET":
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    
  

    
  
