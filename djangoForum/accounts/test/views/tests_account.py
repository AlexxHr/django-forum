from django.contrib import auth
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestAccount(TestCase):
    def test_user_registering_logs_you_in(self):
        response = self.client.post(reverse('account register'),
                                   {'email': 'test@abv.bg', 'username': 'test', 'password1': 'testpassword',
                                    'password2': 'testpassword'})
        user = auth.get_user(self.client)
        self.assertEqual(user.is_authenticated, True)

    def test_user_registering_redirects_to_home(self):
        response = self.client.post(reverse('account register'),
                                   {'email': 'test@abv.bg', 'username': 'test', 'password1': 'testpassword',
                                    'password2': 'testpassword'})
        self.assertRedirects(response, reverse('home'))





