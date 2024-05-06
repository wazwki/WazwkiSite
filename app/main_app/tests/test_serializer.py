''' Tests for serializers '''

from django.test import TestCase

from main_app.models import Contact
from main_app.serializers import ContactSerializer


class ContactSerializerTestCase(TestCase):
    ''' Test case for ContactSerializer '''
    def test_work(self):
        """
        Test the ContactSerializer by creating a Contact object with specific attributes and
        comparing the serialized data to a dictionary with expected values.

        This test case creates a Contact object with the following attributes:
        - mail: 'vazkildi'
        - telegram: 'wazwki'
        - vacancy: 'http://test.ru'
        - description_vacancy: 'test'

        It then serializes the Contact object using the ContactSerializer and compares the
        resulting serialized data to a dictionary with expected values.

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None

        Raises:
        - AssertionError: If the serialized data does not match the expected dictionary.
        """
        contact_test = Contact.objects.create(mail='vazkildi@gmail.com',
            telegram='wazwki', vacancy='http://test.ru', description_vacancy='test')
        serializer_data = ContactSerializer(contact_test).data
        data = {'id': 6, 'mail': 'vazkildi@gmail.com',
            'telegram': 'wazwki', 'vacancy': 'http://test.ru', 'description_vacancy': 'test'}
        self.assertEqual(serializer_data, data)
