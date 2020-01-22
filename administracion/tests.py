from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import login

class Login_Logout_test(TestCase):

    def setUp(self):
        
        User.objects.create(username="testuser", password="hola1234")
        self.client = Client()
        self.user = User.objects.get(username="testuser")
    
    def test_logout(self):

        self.client.login(username="testuser", password="hola1234")
        reverse('logout')