from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password="abc123")
    
    def test_user_pw(self):
        checked = self.user_a.check_password("abc123")
        self.assertTrue(checked)
