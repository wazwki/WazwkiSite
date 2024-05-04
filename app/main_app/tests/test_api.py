''' Tests for mainapp '''
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from main_app.models import Contact
from main_app.serializers import ContactSerializer


class ContactApiTestCase(APITestCase):
    ''' Testing api contact form '''
    def setUp(self):
        self.contact_test = Contact.objects.create(mail='vazkildi@gmail.com', telegram='wazwki', vacancy='test.com', description_vacancy='test')
    def test_get(self):
        url = reverse('contact-list')
        response = self.client.get(url)
        serializer_data = ContactSerializer(self.contact_test).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([serializer_data], response.data)
