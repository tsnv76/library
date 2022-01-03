import io

from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.serializers import Serializer, CharField, IntegerField, ValidationError
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from .serializers import AuthorModelSerializer, BioModelSerializer, BookModelSerializer
from .models import Author, Bio, Book
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions, BasePermission
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class AuthorModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # permission_classes = [DjangoModelPermissions]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BioViewSet(ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioModelSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class AuthorAPIView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


# class AuthorViewSet(ListModelMixin, DestroyModelMixin, GenericViewSet):
    # def perform_destroy(self, instance):
        #     instance.is_active = True
        #     instance.save()

class Pagination(LimitOffsetPagination):
    default_limit = 2


class AuthorViewSet(ListModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name']
    # pagination_class = Pagination

    @action(methods=['GET'], detail=True)
    def get_author_name(self, request, pk=None):
        author = Author.objects.get(pk=pk)
        return Response({'name': str(author)})


class BioModelViewSet(ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

