from .views import AuthorModelViewSet
from django.urls import path

app_name = 'authors'

urlpatterns = [
    path(r'', AuthorModelViewSet.as_view({'get': 'list'}))
]