from rest_framework import serializers
from api.models import Snippet, user


class userserial(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        read_only_fields = ['id']


