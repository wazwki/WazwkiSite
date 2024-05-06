''' Test for API endpoints related to the Contact model '''
import json

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from main_app.models import Contact
from main_app.serializers import ContactSerializer


class ContactApiTestCase(APITestCase):
    """
    Test case for API endpoints related to the Contact model.
    !!!For testing this case need turn off the permission_classes in api.py!!!
    """
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
        self.user = User.objects.create_user(username='TestApi', password='testing123')
        self.contact_test = Contact.objects.create(mail='vazkildi@gmail.com',
            telegram='wazwki', vacancy='test.com', description_vacancy='test')
    def test_get(self):
        """
        Test the GET method of the contact-list endpoint.

        This function sends a GET request to the 'contact-list' endpoint 
        and checks if the response status code is 200 (OK). It also checks
        if the response data matches the serialized data of the contact_test object.

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        url = reverse('contact-list')
        response = self.client.get(url)
        serializer_data = ContactSerializer(self.contact_test).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([serializer_data], response.data)
    def test_post(self):
        """
        Test the POST method of the contact-list endpoint.

        This function sends a POST request to the 'contact-list' endpoint with the provided data 
        and checks if the response status code is 201 (Created).

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        self.client.force_login(user=self.user)
        url = reverse('contact-list')
        data = {
            "mail": "vazkildi@gmail.com",
            "telegram": "wazwki",
            "vacancy": "http://test.ru",
            "description_vacancy": "test"
        }
        json_data = json.dumps(data)
        response = self.client.post(url, json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    def test_put(self):
        """
        Test the PUT method of the contact-detail endpoint.

        This function sends a PUT request to the 'contact-detail' endpoint with the provided data 
        and checks if the response status code is 200 (OK).

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        self.client.force_login(user=self.user)
        url = reverse('contact-detail', args=[self.contact_test.id])
        data = {
            "mail": "vazkildi@gmail.com",
            "telegram": "wazwki",
            "vacancy": "http://test.ru",
            "description_vacancy": "test"
        }
        json_data = json.dumps(data)
        response = self.client.put(url, json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
    def test_delete(self):
        """
        Test the DELETE method of the contact-detail endpoint.

        This function sends a DELETE request to the 'contact-detail' endpoint with 
        the provided contact ID and checks if the response status code is 204 (No Content).

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        self.client.force_login(user=self.user)
        url = reverse('contact-detail', args=[self.contact_test.id])
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
