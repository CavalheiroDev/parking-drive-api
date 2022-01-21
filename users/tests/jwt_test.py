
from rest_framework.test import APITestCase
from django.conf import settings
import jwt

from users.utils import generate_access_token, generate_refresh_token
from users.models import User


class JWTestCase(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(email="email@test.com", password="senhaMuitoForte1234!#")

    def test_generate_access_token(self):
        test_access_token = generate_access_token(self.test_user)
        test_payload = jwt.decode(test_access_token, settings.SECRET_KEY, algorithms=['HS256'])
        
        self.assertEqual(self.test_user.id, test_payload.get("user_id"))
    
    def test_generate_refresh_token(self):
        test_refresh_token = generate_refresh_token(self.test_user)
        test_payload = jwt.decode(test_refresh_token, settings.SECRET_KEY, algorithms=['HS256'])

        self.assertEqual(self.test_user.id, test_payload.get("user_id"))
