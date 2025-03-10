from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mail_sender.urls'), name='sender'),
    path('accounts/', include('accounts.urls'), name='accounts'),
]
