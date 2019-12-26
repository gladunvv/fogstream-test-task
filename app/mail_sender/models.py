from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class MessageForAdmin(models.Model):

    MESSAGE_STATUS = (
        (1, 'Pending'),
        (2, 'Done'),
        (3, 'Sending error')
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    theme = models.CharField(max_length=64)
    text = models.TextField(max_length=255)
    date_send = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=MESSAGE_STATUS, default=1)

    def send(self):
        self.status = 2
        self.date_send = timezone.now()
        self.save()

    class Meta:

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'Message from {self.author}'
