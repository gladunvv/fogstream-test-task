import sys

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from mail_sender.forms import MessageForm
from mail_sender.models import MessageForAdmin
from mail_sender.mail_send import message_send


class MessageForAdminView(TemplateView):

    template_name = 'mail_sender/sender.html'

    def get(self, request, *args, **kwargs):
        form = MessageForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        user = request.user
        if form.is_valid():
            theme = form.cleaned_data['theme']
            text = form.cleaned_data['text']
            message = MessageForAdmin(
                author=user,
                theme=theme,
                text=text
            )
            message.save()
            try:
                message_send(message)
            except Exception as ex:
                message.status = 3
                message.save()
                exception_type = type(ex).__name__
                sys.stdout.write(f'Message error: {exception_type}')
            else:
                message.send()
                context = {
                    'form': form,
                }
                return render(request, self.template_name, context)       
        context = {
            'form': form,
            'error': 'Error send, sorry, something went wrong'
        }
        return render(request, self.template_name, context)
