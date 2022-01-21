
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(email="email@test.com", password="senhaMuitoForte1234!#")
        self.profile_url = "/accounts/profile/"
        self.url_token = "/accounts/token/"
        self.url_refresh_token = "/accounts/refresh-token/"
        self.login_data = {"login": "email@test.com", "password": "senhaMuitoForte1234!#"}
        self.expected_response_data_user = {
            "email": "email@test.com", 
            "username": None, 
            "cpf": None, 
            "first_name": None, 
            "last_name": None, 
            "is_staff": False, 
            "is_active": True
        }
    

    def test_login(self):
        response = self.client.post(self.url_token, data=self.login_data)

        self.assertContains(response, "access_token")
        self.assertContains(response, "user")
        self.assertEqual(response.json().get("user"), self.expected_response_data_user)
        self.assert_("refresh_token" in response.cookies)

    def test_get_profile(self):
        self.client.force_authenticate(self.test_user)
        response = self.client.get(self.profile_url)

        self.assertEqual(response.json().get("user"), self.expected_response_data_user)
