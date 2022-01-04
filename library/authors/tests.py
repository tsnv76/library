from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from .views import AuthorModelViewSet
from django.contrib.auth.models import User
from .models import Author, Bio
from mixer.backend.django import mixer


class TestAuthorView(APITestCase):

    def setUp(self) -> None:
        self.admin = User.objects.create_superuser('admin', email='test@test.ru', password='123')

    def test_get_list(self):
        factory = APIRequestFactory()
        author = mixer.blend(Author, birthday_year=1799)
        # author = mixer.blend(Author)

        # request = factory.post('/api/authors/', {
        #     'first_name': 'Александр',
        #     'last_name': 'Пушкин',
        #     'birthday_year': 1799
        # })
        # force_authenticate(request, user=self.admin)
        # view = AuthorModelViewSet.as_view({'post': 'create'})
        # response = view(request)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.data['last_name'], 'Пушкин')

        request = factory.get('/api/authors/')
        force_authenticate(request, user=self.admin)
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)
        # self.assertEqual(response.data['last_name'], 'Пушкин')
        self.assertEqual(response.data['birthday_year'], 1799)

    def test_client_get_list(self):
        self.client.login(username='admin', password='123')
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # response = self.client.post('/api/authors/', {
        #             'first_name': 'Александр',
        #             'last_name': 'Пушкин',
        #             'birthday_year': 1799
        #             })
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.data['last_name'], 'Пушкин')

        self.client.logout()
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_client_bio(self):
        bio = mixer.blend(Bio, author__birthday_year=1800)
        self.client.login(username='admin', password='123')
        response = self.client.get('/api/bio/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


