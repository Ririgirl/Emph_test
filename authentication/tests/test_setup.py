from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake = Faker()

        self.user_data = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'testuser@example.com',
            'password': 'superpassword'
        }

        # import pdb
        # pdb.set_trace()

        return super().setUp()

    def tearDown(self):
        return super().tearDown()