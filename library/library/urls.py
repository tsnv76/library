from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from authors.views import AuthorViewSet, get_view, post_view, BioViewSet


# router = SimpleRouter()
router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('bios', BioViewSet)

#  /authors/   GET, POST
#  /authors/1/ GET, PUT/PATCH, DELETE


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/get/', get_view),
    path('api/post/', post_view)
]
