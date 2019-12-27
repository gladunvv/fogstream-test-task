from django.core.mail import EmailMessage, mail_admins
from django.template.loader import render_to_string


def message_send(message_data, *args, **kwargs):
    author = message_data.author.username
    theme = message_data.theme
    text = message_data.text
    mail_subject = f'Message from {author}'
    message = render_to_string('message/admin_message.html',{
        'author': author,
        'theme': theme,
        'text': text
    })
    mail_admins(mail_subject, message, html_message=message)