from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from faker import Factory
from app_dir.factories import BookFactory, UserFactory

faker = Factory.create()


class BookApiTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.book = BookFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.namespace = 'book_api'
        self.body = {
            'name': faker.word(),
            'description': faker.text()
        }
        self.create_url = reverse(self.namespace + ':create')
        self.list_url = reverse(self.namespace + ':list')
        self.update_url = reverse(self.namespace + ':update', kwargs={'pk': self.book.id})

    def test_create_book_api(self):
        response = self.client.post(self.create_url, self.body, format='json')
        self.assertEqual(201, response.status_code)

    def test_list_books_api_without_parameters(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, self.book)

    def test_listing_book_api_with_parameters(self):
        response = self.client.get(self.list_url + '?page_size=10&q=' + self.book.name)
        self.assertContains(response, self.book)

    def test_update_book_api(self):
        response = self.client.put(self.update_url, self.body)
        self.assertEqual(200, response.status_code)
