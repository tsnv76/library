import io

from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer, CharField, IntegerField, ValidationError
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from .serializers import AuthorModelSerializer, BioModelSerializer
from .models import Author, Bio, Book


class AuthorViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BioViewSet(ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioModelSerializer


#  [Client] -> [Router/URL] -> [View] -> [Serializer] -> [Model]

class AuthorSerializer(Serializer):
    id = IntegerField()
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    birthday_year = IntegerField()

    def validate_birthday_year(self, value):
        if value < 1000:
            raise ValidationError('Value must be gt 1000')
        return value

    def validate(self, attrs):
        if attrs['last_name'] == 'Достоевский' and attrs['birthday_year'] != 1821:
            raise ValidationError('birthday_year must be 1821')
        return attrs

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        instance.save()
        return instance

    def create(self, validated_data):
        author = Author(**validated_data)
        author.save()
        return author


class BioSerializer(Serializer):
    text = CharField(max_length=64)
    author = AuthorSerializer()


class BookSerializer(Serializer):
    text = CharField(max_length=64)
    authors = AuthorSerializer(many=True)


# def get_view(request):
    # author = Author.objects.get(pk=1)
    # serializer = AuthorSerializer(author)
    # render = JSONRenderer()
    # json_data = render.render(serializer.data)
    # return HttpResponse(json_data)

# def get_view(request):
    # bio = Bio.objects.get(pk=1)
    # serializer = BioSerializer(bio)
    # render = JSONRenderer()
    # json_data = render.render(serializer.data)
    # print(serializer.data)
    # return HttpResponse(json_data)

def get_view(request):
    bio = Book.objects.get(pk=1)
    serializer = BookSerializer(bio)
    render = JSONRenderer()
    json_data = render.render(serializer.data)
    print(serializer.data)
    return HttpResponse(json_data)



@csrf_exempt
def post_view(request):
    print(request.body)
    data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = AuthorSerializer(data=data)
    elif request.method == 'PUT':
        author = Author.objects.get(pk=3)
        serializer = AuthorSerializer(author, data=data)
    elif request.method == 'PATCH':
        author = Author.objects.get(pk=3)
        serializer = AuthorSerializer(author, data=data, partial=True)

    if serializer.is_valid():
        print(serializer.validated_data)

        author = serializer.save()
        serializer = AuthorSerializer(author)
        render = JSONRenderer()
        json_data = render.render(serializer.data)
        print(serializer.data)
        return HttpResponse(json_data)
    else:
        return HttpResponseServerError(serializer.errors['non_field_errors'])







    # author = Author.objects.get(pk=1)
    # serializer = AuthorSerializer(author)
    # render = JSONRenderer()
    # json_data = render.render(serializer.data)
    # print(serializer.data)
    # return HttpResponse(json_data)

