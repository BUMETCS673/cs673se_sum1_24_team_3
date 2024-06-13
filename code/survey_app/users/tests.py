from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTestCase(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(username='testuser', password='password')

    def test_user_creation(self):
        user = get_user_model().objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')

    def test_user_login(self):
        login = self.client.login(username='testuser', password='password')
        self.assertTrue(login)
