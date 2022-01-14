from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from authors.views import AuthorModelViewSet, AuthorViewSet, BioViewSet, AuthorAPIView, BookViewSet

# get_view, post_view, BioViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='Library',
        default_version='v1',
        description='',
        contact=openapi.Contact(email='test@test.com'),
        license=openapi.License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

# router = SimpleRouter()
router = DefaultRouter()
router.register('authors', AuthorModelViewSet, basename='authors')
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
    re_path(r'^api/(?P<version>.\d)', AuthorModelViewSet.as_view({'get': 'list'})),
    path('api/authors/v1', include('authors.urls', namespace='v1')),
    path('api/authors/v2', include('authors.urls', namespace='v2')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0)),

    # path('api/get/', AuthorViewSet.as_view({'get': 'list'})),
    # path('api/get/<int:pk>/', AuthorAPIView.as_view()),
    # path('api/post/', post_view)
]
