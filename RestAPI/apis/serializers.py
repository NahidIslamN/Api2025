from rest_framework import serializers
from .models import Person



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError("Age cannot be less than 18")
        elif data['age'] > 32:
            raise serializers.ValidationError("Age cannot be greater than 32")
        return data
        
    

    
        