from .test_setup import TestSetUp
from django.contrib.auth.models import User


class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res = self.client.post(
            self.register_url, self.user_data, format="json")
        self.assertEqual('username', self.user_data['username'])
        self.assertEqual('first_name', self.user_data['first_name'])
        self.assertEqual('last_name', self.user_data['last_name'])
        self.assertEqual('testuser@example.com', self.user_data['email'])
        self.assertEqual('superpassword', self.user_data['password'])
        self.assertEqual(res.status_code, 201)

    def test_user_can_login_after_verification(self):
        response = self.client.post(
            self.register_url, self.user_data, format="json")
        username = response.data['username']
        user = User.objects.get(username=username)
        user.is_verified = True
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)
