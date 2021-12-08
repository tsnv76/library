from .models import Author
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import ModelSerializer


# class AuthorSerializer(HyperlinkedModelSerializer):
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

