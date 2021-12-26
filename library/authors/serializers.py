from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField
from .models import Author, Bio, Book


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BioModelSerializer(ModelSerializer):
    # author = AuthorModelSerializer()
    author = StringRelatedField()

    class Meta:
        model = Bio
        fields = '__all__'


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
