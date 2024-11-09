from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_us, name='contact'),
    path('messages/', views.contact_messages, name='messages'),
    path('contact/messages/reply/<int:message_id>/', views.reply_contact_message, name='reply_contact_message'),
]
