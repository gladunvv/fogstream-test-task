from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from mail_sender.forms import MessageForm
from mail_sender.models import MessageForAdmin
from mail_sender.mail_send import message_send


class MessageForAdminView(LoginRequiredMixin, TemplateView):

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
                exception_value = list(ex.args)
                print(f'Message error: {exception_type}\n Traceback except: {exception_value}')
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
