
from django.urls import path
from mail_sender.views import MessageForAdminView

app_name = 'sender'
urlpatterns = [
    path('', MessageForAdminView.as_view(), name='index')
    ]
