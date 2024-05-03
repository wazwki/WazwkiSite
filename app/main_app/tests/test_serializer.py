''' Tests for serializers '''

from django.test import TestCase

from main_app.models import Contact
from main_app.serializers import ContactSerializer


class ContactSerializerTestCase(TestCase):
    ''' Test for serializer contact form '''
    def test_work(self):
        contact_test = Contact.objects.create(mail='vazkildi', telegram='wazwki', vacancy='test', description_vacancy='test')
        serializer_data = ContactSerializer(contact_test).data
        data = {'id': 1, 'mail': 'vazkildi@gmail.com', 'telegram': 'wazwki', 'vacancy': 'test', 'description_vacancy': 'test'}
        self.assertEqual(serializer_data, data)
