from django.urls import path
from chatbot import views

urlpatterns = [
    path('', views.chatbot, name='chatbot')
]