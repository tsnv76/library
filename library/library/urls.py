from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views

from authors.views import AuthorModelViewSet, AuthorViewSet, BioViewSet, AuthorAPIView, BookViewSet

# get_view, post_view, BioViewSet

# router = SimpleRouter()
router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('bios', BioViewSet),
router.register('books', BookViewSet)

#

# router.register('authors', AuthorViewSet)
# router.register('bios', BioViewSet)

#  /authors/   GET, POST
#  /authors/1/ GET, PUT/PATCH, DELETE


# http://127.0.0.1:8000/api/authors/?name=Сергей

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    # path('api/get/', AuthorViewSet.as_view({'get': 'list'})),
    # path('api/get/<int:pk>/', AuthorAPIView.as_view()),
    # path('api/post/', post_view)
]
