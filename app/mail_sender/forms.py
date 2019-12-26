from django import forms
from mail_sender.models import MessageForAdmin


class MessageForm(forms.ModelForm):

    class Meta:
        model = MessageForAdmin
        fields = ['theme', 'text']