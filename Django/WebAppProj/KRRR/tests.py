from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.admin_url = reverse('admin-admin')
        self.cart_url = reverse('cart')
        self.shop_url = reverse('shop')

        self.user = {
            'first_name':'John',
            'last_name':'Doe',
            'username':'DOE',
            'email':'jogn@doe.com',
            'password1':'tesing123',
            'password2':'testig123',
        }

        return super().setUp()


class AuthTest(BaseTest):

    # can unlogged user access register page
    def test_can_access_register_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'KRRR/register.html')

    # can unlogged user register a new account
    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)

    # can unlogged user access login page
    def test_can_access_login_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    # can user successfully log in
    def test_login_success(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)

    # can unlogged user access public endpoint (shop)
    def test_can_access_public_endpoint(self):
        response = self.client.get(self.shop_url)
        self.assertEqual(response.status_code, 200)


    # Response status code for the following three should be 302, because
    # the user is redirected to the login page and this is the code
    # Django returns in this case 
    # (source: https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpResponseRedirect)
  
    # is endpoint with user-level authorization unavaiable for unlogged user
    def test_cannot_access_user_endpoint(self):
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, 302)

    # is admin site unavaiable for unlogged user
    def test_can_anon_find_admin(self):
        response = self.client.get(self.admin_url)
        self.assertEqual(response.status_code, 302)

    # is admin site unavaiable for user without admin privileges
    def test_cannot_access_admin_endpoint(self):
        self.client.post(self.register_url, self.user, format="text/html")
        self.client.post(self.login_url, self.user, format="text/html")
        response = self.client.get(self.admin_url)
        self.assertEqual(response.status_code, 302)


    

  


