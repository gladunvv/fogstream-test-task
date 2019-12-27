from django import template

from mail_sender.models import MessageForAdmin

register = template.Library()

@register.inclusion_tag('messages.html', takes_context=True)
def messages(context, menu):
    message_done = MessageForAdmin.objects.all()
    message_error = MessageForAdmin.objects.filter(status=3)
    context = {
        'message_done': len(message_done),
        'message_error': len(message_error)
    }
    return context