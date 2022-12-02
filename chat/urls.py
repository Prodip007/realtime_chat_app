from django.urls import path, include

from .views import ChatSessionView, ChatSessionMessageView

urlpatterns = [
    path('chats/', ChatSessionView.as_view(), name='chat_session'),
    path('chats/<uri>/', ChatSessionView.as_view(), name='chat_session_patch'),
    path('chats/<uri>/messages/', ChatSessionMessageView.as_view(), name='chat_session_message')
]