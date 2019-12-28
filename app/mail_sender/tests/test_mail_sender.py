from django.urls import reverse
from django.core import exceptions
from django.test import TestCase, Client
from django.contrib.auth import get_user_model, login
from mail_sender.models import MessageForAdmin
from mail_sender.mail_send import message_send
from mail_sender.templatetags.messages import messages


INDEX_PAGE_URL = reverse('sender:index')

def create_user(*args, **kwargs):
    context = {
        'username': 'newuser',
        'password': 'newpass1234',
    }
    return get_user_model().objects.create_user(**context)


class MailSenderTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_message_models_str_method(self):
        user = create_user()
        context = {
            'author': user,
            'theme': 'Admin message',
            'text': 'Dear admin, help me',
        }
        message = MessageForAdmin.objects.create(**context)

        self.assertEqual(str(message), 'Message from newuser')

    def test_index_get(self):
        res = self.client.get(INDEX_PAGE_URL, follow=True)
        self.assertEqual(res.status_code, 200)

    def test_message_create_object_success(self):
        user = create_user()
        context = {
            'author': user,
            'theme': 'Admin message',
            'text': 'Dear admin, help me',
        }
        message = MessageForAdmin.objects.create(**context)

        self.assertEqual(message.theme, context['theme'])

    def test_message_send_object_success(self):
        user = create_user()
        context = {
            'author': user,
            'theme': 'Admin message',
            'text': 'Dear admin, help me',
        }
        message = MessageForAdmin.objects.create(**context)
        message.send()

        self.assertEqual(message.status, 2)

    def test_message_post_view_success(self):
        create_user()
        context = {
            'theme': 'Admin message',
            'text': 'Dear admin, help me'
        }
        self.client.login(username='newuser', password='newpass1234')
        res = self.client.post(INDEX_PAGE_URL, context, follow=True)
        message = MessageForAdmin.objects.get(theme=context['theme'])
        self.assertEqual(message.status, 2)
    
    def test_mail_send(self):
        user = create_user()
        context = {
            'author': user,
            'theme': 'Admin message',
            'text': 'Dear admin, help me',
        }
        message = MessageForAdmin.objects.create(**context)
        status = message_send(message)
        self.assertEqual(status, 'success')

    def test_message_post_invalid_data(self):
        create_user()
        context = {
            'theme': 'Admin message'*10,
            'text': 'Dear admin, help me'
        }
        self.client.login(username='newuser', password='newpass1234')
        res = self.client.post(INDEX_PAGE_URL, context, follow=True)
        self.assertEqual(res.context['error'],'Error send, sorry, something went wrong' )
    
    def test_template_tags(self):
        user = create_user()
        context = {
            'author': user,
            'theme': 'Admin message',
            'text': 'Dear admin, help me',
        }
        message = MessageForAdmin.objects.create(**context)
        template_data = messages()
        self.assertEqual(template_data['message_done'], 1)
        self.assertEqual(template_data['message_error'], 0)
