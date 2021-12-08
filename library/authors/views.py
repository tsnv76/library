from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer
from .models import Author


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
