from django.urls import reverse
from django.core import exceptions
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


SIGNUP_URL = reverse('accounts:signup')
LOGIN_URL = reverse('accounts:login')
LOGOUT_URL = reverse('accounts:logout')

INDEX_PAGE_URL = reverse('sender:index')

def create_user(*args, **kwargs):
    context = {
        'username': 'newuser',
        'password': 'newpass1234',
    }
    return get_user_model().objects.create_user(**context)

class AccountsTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_signup_get(self):
        res = self.client.get(SIGNUP_URL)
        self.assertEqual(res.status_code, 200)

    def test_signup_accounts_success(self):
        context = {
            'username': 'newuser',
            'password1': 'newpass1234',
            'password2': 'newpass1234'
        }
        res = self.client.post(SIGNUP_URL, context, follow=True)      
        user = get_user_model().objects.get(username=context['username'])
        self.assertEqual(res.status_code, 200)
        self.assertEqual(user.username, context['username'])

    def test_signup_redirect_success(self):
        context = {
            'username': 'newuser',
            'password1': 'newpass1234',
            'password2': 'newpass1234'
        }
        res = self.client.post(SIGNUP_URL, context, follow=True)
        self.assertRedirects(res, LOGIN_URL, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_signup_failed_password(self):
        context = {
            'username': 'newuser',
            'password1': 'newpass1234',
            'password2': 'newpass4321'
        }
        res = self.client.post(SIGNUP_URL, context, follow=True)

        with self.assertRaises(get_user_model().DoesNotExist):
            get_user_model().objects.get(username=context['username'])
        
    def test_signup_failed_username(self):
        context = {
            'username': '',
            'password1': 'newpass1234',
            'password2': 'newpass1234'
        }
        res = self.client.post(SIGNUP_URL, context, follow=True)
        with self.assertRaises(get_user_model().DoesNotExist):
            get_user_model().objects.get(username=context['username'])

    def test_signup_form_success(self):
        context = {
            'username': 'newuser',
            'password1': 'newpass1234',
            'password2': 'newpass1234'
        }
        form = UserCreationForm(context)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, 'newuser')

    def test_signup_form_password_failed(self):
        context = {
            'username': 'newuser',
            'password1': 'newpass1234',
            'password2': 'newpass4321'
        }
        form = UserCreationForm(context)
        self.assertFalse(form.is_valid())
        self.assertDictEqual(form.errors, {'password2':['The two password fields didn’t match.']})

    def test_login_get(self):
        res = self.client.get(LOGIN_URL)
        self.assertEqual(res.status_code, 200)

    def test_login_success(self):
        context = {
            'username': 'newuser',
            'password': 'newpass1234',
        }
        create_user()
        res = self.client.post(LOGIN_URL, context, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.context['user'].is_active)

    def test_login_failed(self):
        context = {
            'username': 'newuser',
            'password': 'newpass4321',
        }
        create_user()
        res = self.client.post(LOGIN_URL, context, follow=True)
        self.assertFalse(res.context['user'].is_active)

    def test_login_success_redirect(self):
        context = {
            'username': 'newuser',
            'password': 'newpass1234',
        }
        create_user()
        res = self.client.post(LOGIN_URL, context, follow=True)
        self.assertRedirects(res, INDEX_PAGE_URL, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_logout(self):
        context = {
            'username': 'newuser',
            'password': 'newpass1234',
        }
        create_user()
        res_login = self.client.post(LOGIN_URL, context, follow=True)
        self.assertTrue(res_login.context['user'].is_active)
        res_logout = self.client.get(LOGOUT_URL, follow=True)
        self.assertFalse(res_logout.context['user'].is_active)
