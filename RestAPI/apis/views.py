from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apis.models import *
from apis.serializers import *
# Create your views here.

@api_view(['GET',"POST","PUT","DELETE"])
def persons(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serialis = PersonSerializer(data = request.data)
        if serialis.is_valid():
            serialis.save()
            return Response(serialis.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialis.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        persons = Person.objects.get(id = request.data["id"])
        serializer = PersonSerializer(instance=persons, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == "DELETE":
        persons = Person.objects.get(id = request.data["id"])
        persons.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
