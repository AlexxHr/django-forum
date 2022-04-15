from django.contrib import auth
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestErrors(TestCase):
    def test_when_404(self):
        response = self.client.get('/test/wrong')
        self.assertTemplateUsed(response, '404.html')

    # def test_when_403(self):
    #     account = UserModel.objects.create(email='test@abv.bg', username='test', password='testpassword')
    #     test = auth.get_user(self.client)
    #     response = self.client.get('/profile/1/edit')
    #     self.assertTemplateUsed(response, '403.html')
