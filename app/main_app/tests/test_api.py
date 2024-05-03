''' Tests for mainapp '''
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from main_app.models import Contact
from main_app.serializers import ContactSerializer


class ContactApiTestCase(APITestCase):
    ''' Testing api contact form '''
    def test_get(self):
        contact_test = Contact.objects.create(mail='vazkildi@gmail.com', telegram='wazwki', vacancy='test', description_vacancy='test')
        url = reverse('contact-list')
        response = self.client.get(url)
        serializer_data = ContactSerializer(contact_test).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([serializer_data], response.data)
