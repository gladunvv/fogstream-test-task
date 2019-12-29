from django import template

from mail_sender.models import MessageForAdmin

register = template.Library()


@register.inclusion_tag('messages.html', takes_context=True)
def messages(context, message):
    message_done = MessageForAdmin.objects.all()
    message_error = message_done.filter(status=3)
    message_count = {
        'message_done': message_done.count(),
        'message_error': message_error.count()
    }
    return message_count
