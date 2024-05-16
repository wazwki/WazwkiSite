''' Tests for serializers '''

from django.test import TestCase
from django.contrib.auth.models import User


from main_app.models import Contact
from main_app.serializers import ContactSerializer


class ContactSerializerTestCase(TestCase):
    ''' Test case for ContactSerializer '''
    def setUp(self):
        """
        Set up the test environment by creating a test instance of 
        the Contact model with the following attributes:
        
        - mail: 'vazkildi@gmail.com'
        - telegram: 'wazwki'
        - vacancy: 'test.com'
        - description_vacancy: 'test'
        
        This method is called before each test case is run.
        """
        self.user = User.objects.create_user(username='TestSerializer', password='testing123')
        self.contact_test = Contact.objects.create(mail='vazkildi@gmail.com',
            telegram='wazwki', vacancy='test.com', description_vacancy='test', owner=self.user)

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
        serializer_data = ContactSerializer(self.contact_test).data
        data = {'id': self.contact_test.id, 'mail': 'vazkildi@gmail.com',
            'telegram': 'wazwki', 'vacancy': 'test.com', 'description_vacancy': 'test', 'owner': self.contact_test.owner.id}
        print("serializer_data:", serializer_data, "data:", data)
        self.assertEqual(serializer_data, data)
