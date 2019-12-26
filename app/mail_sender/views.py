from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from mail_sender.forms import MessageForm
from mail_sender.models import MessageForAdmin

class MessageForAdminView(TemplateView):

    template_name = 'mail_sender/sender.html'

    def get(self, request, *args, **kwargs):
        form = MessageForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = request.user
        form = MessageForm(request.POST)
        if form.is_valid():
            message = MessageForAdmin(
                author=user,
                theme=form.cleaned_data['theme'],
                text=form.cleaned_data['text']
            )
            message.save()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
